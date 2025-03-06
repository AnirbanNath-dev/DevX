from typing import cast
import wavelink
from discord.ext import commands
import discord

class Loop(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def loop(self, ctx: commands.Context) -> None:
        """Loop the current song."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        # Get the current track before looping
        current_track = player.current
        
        player.queue.loaded = wavelink.QueueMode.loop
    
        embedVar = discord.Embed(
            title="Song Loop",
            description=f"The song **{current_track}** has been looped.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embedVar)

async def setup(bot : commands.Bot):
    await bot.add_cog(Loop(bot))

    print("Loop cog loaded.")