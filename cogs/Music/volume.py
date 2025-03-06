from typing import cast, Optional
import wavelink
from discord.ext import commands
import discord

class Volume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def volume(self, ctx: commands.Context, value: Optional[int]) -> None:
        """Change the volume of the player."""
        if value is None:
            embedVar = discord.Embed(
                title="Volume Command Help",
                description="The `?volume` command allows you to change the volume of the player. To use the command, type `?volume` followed by a value between 10 and 200. For example, `?volume 100`.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embedVar)
            return

        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        # Check if the volume value is within the valid range
        if 10 <= value <= 200:
            await player.set_volume(value)
            await ctx.message.add_reaction("\u2705")

            # Create an embed message
            embedVar = discord.Embed(
                title="Volume Changed",
                description=f"The volume has been set to **{value}**.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Please enter a volume value between 10 and 200.")

async def setup(bot : commands.Bot):
    await bot.add_cog(Volume(bot))
    print("Volume cog loaded.")