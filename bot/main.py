import discord
from discord.ext import commands 
from math import floor
from bot.settings import (
    TOKEN , 
    PREFIX , 
    COGS , 
    WAVELINK_PASS , 
    WAVELINK_URI
)
import os
from postgres.db import setup_db , close_db
from asyncpg import Connection
import wavelink
from bot.utils.buttons import (
    Pause,
    Resume,
    Skip
)

class DevX(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX , intents=discord.Intents.all())
        

    async def on_ready(self) -> None:

        self.remove_command("help")
        await load_cog()
        self.db : Connection = await setup_db()
        print(f"Logged in as {self.user}")
        
    async def setup_hook(self):
        
        nodes = [wavelink.Node(uri=WAVELINK_URI, password=WAVELINK_PASS)]
        await wavelink.Pool.connect(nodes=nodes, client=self)
    
    async def on_wavelink_node_ready(
        self, payload: wavelink.NodeReadyEventPayload
    ) -> None:
        print(f"Wavelink Node connected: {payload.node!r} | Resumed: {payload.resumed}")

    async def on_wavelink_track_start(
        self, payload: wavelink.TrackStartEventPayload
    ) -> None:
        player: wavelink.Player | None = payload.player
        if not player:
            return
        
        track: wavelink.Playable = payload.track

        track_length_ms = int(track.length)
        mins = track_length_ms // 60000  
        secs = (track_length_ms % 60000) // 1000 

        embed = discord.Embed(
            title="<a:music_disc:1347098774203269142> Now Playing" , 
            color=discord.Color.green()
        )

        embed.add_field(name="Song" , value=f"[`{track.title}`]({track.uri})" , inline=True)
        embed.add_field(name="Artist" , value=f"`{track.author}`",inline=True)
        embed.add_field(name="Duration" , value=f"`{floor(mins) if mins>=10 else f"0{floor(mins)}"}:{floor(secs) if secs>=10 else f"0{floor(secs)}"}`" , inline=True)
        if track.artwork:
            embed.set_thumbnail(url=track.artwork)

       
        pause = Pause()
        resume = Resume()
        skip = Skip()

        views = discord.ui.View()
        views.add_item(pause)
        views.add_item(resume)
        views.add_item(skip)    

        await player.home.send(embed=embed , view=views)

    async def on_wavelink_inactive_player(
        self, player: wavelink.Player
    ) -> None:
        await player.channel.send(f"The player has been inactive for `{player.inactive_timeout}` seconds. Goodbye!")
        await player.disconnect()
        
    
bot = DevX()
        
    
async def load_cog():
    for list in os.listdir("cogs"):
        if list.endswith(".py"):
                
             await bot.load_extension(f"cogs.{list[:-3]}")
        
    for dir in COGS:
        try:
            for fn in os.listdir(f"cogs/{dir}"):
                if fn.endswith(".py"):
                    await bot.load_extension(f"cogs.{dir}.{fn[:-3]}")
        except FileNotFoundError:
            print(f"Error in loading {dir} cogs dir.")        

@bot.event
async def on_message(message : discord.Message):
    
    if message.author.bot:
        return
    
    await bot.process_commands(message)

@bot.hybrid_command()
async def sync(ctx: commands.Context):

    synced = await bot.tree.sync()

    if len(synced)>0:
        for cmd in synced:
            await ctx.send(f"Synced {cmd}")

        await ctx.send(f"Synced {len(synced)}commands globally!")
    else:
        await ctx.send("No slash commands to register.")

    
@bot.hybrid_command()
async def shutdown(ctx : commands.Context):
    
    if str(ctx.author.id) not in ["1288870270664179815"]:
        
        return await ctx.send(":( You need to be the developer of the bot to shut it down!")
    
    await ctx.send("Good bye!")
    await close_db(bot.db)
    await bot.close()

@bot.command()
async def ping(ctx : commands.Context):
    await ctx.send(f"🏓 Pong! {bot.user.name} is online. Latency - **{round(bot.latency * 1000)}ms**")
    
    
def run():
    bot.run(token=TOKEN)

if __name__ == "__main__":
    run()
