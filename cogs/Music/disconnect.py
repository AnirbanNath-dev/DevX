from typing import cast
import wavelink
from discord.ext import commands


class Disconnect(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.hybrid_command(aliases=["dc"])
    async def disconnect(self, ctx: commands.Context) -> None:
        """Disconnect the Player."""
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return

        await player.disconnect()
        await ctx.message.add_reaction("\u2705")


async def setup(bot : commands.Bot):
    await bot.add_cog(Disconnect(bot))
    print("Disconnect cog loaded.")