from typing import cast
import wavelink
from discord.ext import commands
import discord

class Daycore(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.daycore_on = False

    @commands.command()
    async def daycore(self, ctx: commands.Context, mode: str = None) -> None:
        """Set the filter to a daycore style."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        if mode is None:
            embedVar = discord.Embed(
                title="Daycore Command",
                description="Use ``?daycore on`` to turn on daycore mode or ``?daycore off`` to turn it off.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embedVar)
            return
        
        if mode.lower() == "on":
            self.daycore_on = True
            filters: wavelink.Filters = player.filters
            filters.timescale.set(pitch=0.8, speed=0.8, rate=1)
            await player.set_filters(filters)
            
        elif mode.lower() == "off":
            self.daycore_on = False
            filters: wavelink.Filters = player.filters
            filters.timescale.set(pitch=1.0, speed=1.0, rate=1)
            await player.set_filters(filters)
            
        else:
            await ctx.send("Invalid mode. Please use '?daycore on' or '?daycore off'.")
            return
        
        await ctx.message.add_reaction("\u2705")
        
