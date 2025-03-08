from typing import cast
import wavelink
from discord.ext import commands
import discord
from bot.settings import PREFIX

class Nightcore(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.nightcore_on = False

    @commands.command()
    async def nightcore(self, ctx: commands.Context, mode: str = None) -> None:
        """Set the filter to a nightcore style."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        if mode is None:
            embed = discord.Embed(
                title="Nightcore Command",
                description=f"Use ``{PREFIX}nightcore on`` to turn on nightcore mode or ``{PREFIX}nightcore off`` to turn it off.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
            return
        
        if mode.lower() == "on":
            self.nightcore_on = True
            filters: wavelink.Filters = player.filters
            filters.timescale.set(pitch=1.2, speed=1.2, rate=1)
            await player.set_filters(filters)
            
        elif mode.lower() == "off":
            self.nightcore_on = False
            filters: wavelink.Filters = player.filters
            filters.timescale.set(pitch=1.0, speed=1.0, rate=1)
            await player.set_filters(filters)
            
        else:
            await ctx.send(f"Invalid mode. Please use '{PREFIX}nightcore on' or '{PREFIX}nightcore off'.")
            return

        await ctx.message.add_reaction("\u2705")
        
