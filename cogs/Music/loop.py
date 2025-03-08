from typing import cast
import wavelink
from discord.ext import commands
import discord

class Loop(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def loop(self, ctx: commands.Context , mode : str = None) -> None:
        """Loop the current song."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return
        if mode is None:
            embedVar = discord.Embed(
                title="Loop Command",
                description="Use ``?loop on`` to turn on loop mode or ``?loop off`` to turn it off.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embedVar)
            return
        # Get the current track before looping
        current_track = player.current
        
        if mode.lower() == "on":
            if player.queue.mode == wavelink.QueueMode.loop:
                await ctx.send(f"{ctx.author.mention} The song `{current_track.title}` is already in loop.")
                return
            
            player.queue.mode = wavelink.QueueMode.loop
            embed = discord.Embed(
                title="Song Loop",
                description=f"Turned on loop for **{current_track.title}**",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            
        elif mode.lower() == "off":
            if player.queue.mode == wavelink.QueueMode.normal:
                await ctx.send(f"{ctx.author.mention} The song `{current_track.title}` is not in loop.")
                return
            
            player.queue.mode = wavelink.QueueMode.normal
            embed = discord.Embed(
                title="Song Loop",
                description=f"Turned on loop for **{current_track.title}**",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("Invalid mode. Please use '?loop on' or '?loop off'.")
            
