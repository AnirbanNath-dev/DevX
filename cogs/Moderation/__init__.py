from bot.main import DevX
from .purge import Purge


async def setup(bot : DevX):
    await bot.add_cog(Purge(bot))