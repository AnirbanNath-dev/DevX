from typing import cast
import wavelink
from discord.ext import commands
import discord

class Skip(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def skip(self, ctx: commands.Context) -> None:
        """Skip the current song."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        # Get the current track before skipping
        current_track = player.current

        await player.skip(force=True)
        await ctx.message.add_reaction("\u2705")

        embed = discord.Embed(
            title="Song Skipped",
            description=f"The song **{current_track if current_track else ""}** has been skipped.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

