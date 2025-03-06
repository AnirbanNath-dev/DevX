from typing import cast
import wavelink
from discord.ext import commands
import discord

class Pause(commands.Cog):
    def __init__(self, bot : commands.Cog):
        self.bot = bot

    @commands.command(aliases=["pause", "resume"])
    async def toggle(self, ctx: commands.Context) -> None:
        """Pause or Resume the Player depending on its current state."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return
        
        # Toggle pause
        await player.pause(not player.paused)

        # Create an embed message
        embedVar = discord.Embed(
            title=f"Pause/Play",
            description=f"The Song is now {'paused' if player.paused else 'playing'}.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embedVar)

async def setup(bot : commands.Cog):
    await bot.add_cog(Pause(bot))
    print("Pause cog loaded.")