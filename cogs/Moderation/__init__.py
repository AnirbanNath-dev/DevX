from bot.main import DevX
from .dm import Dm
from .purge import Purge


async def setup(bot : DevX):
    await bot.add_cog(Dm(bot))
    await bot.add_cog(Purge(bot))