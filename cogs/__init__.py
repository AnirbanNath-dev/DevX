from bot.main import DevX
from .error import ErrorHandler
from .help import Help


async def setup(bot : DevX):
    await bot.add_cog(ErrorHandler(bot))
    await bot.add_cog(Help(bot))