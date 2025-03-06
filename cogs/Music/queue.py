from typing import cast
import wavelink
from discord.ext import commands
import discord

class Queue(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def queue(self, ctx: commands.Context) -> None:
        
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            await ctx.send(embed=discord.Embed(description="I'm currently not playing any song. Please add a song to the queue first."))
            return

        embed = discord.Embed(
            color=0xe882ff,
        )
        embed.add_field(name="<a:music_disc:1347098774203269142> Now Playing" , value=f"[`{player.current.title}`]({player.current.uri})" , inline=False)
        count = player.queue.count
        if player.current.artwork:
            embed.set_thumbnail(url=player.current.artwork)
        if count > 0:
            embed.add_field(
                name="<:cmusic:1346851234082197584> Upcoming Songs:",
                value="\n".join([f"**{i+1}.** `{track.title}` by `{track.author}`" for i, track in enumerate(player.queue)]),
                inline=False
            )
        else:
            embed.add_field(
                name="Queue is Empty!",
                value="There are no upcoming songs in the queue.",
                inline=False
            )
        
        embed.set_footer(text=f"Requested by {ctx.author.name}" , icon_url=ctx.author.avatar.url)
        
        await ctx.send(embed=embed)

async def setup(bot : commands.Bot):
    await bot.add_cog(Queue(bot))

    print("Queue cog loaded.")