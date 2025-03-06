from discord.ext import commands


class Dm(commands.Cog):
    
    def __init__(self , bot : commands.Bot):
        super().__init__()
        self.bot = bot
        
        

async def setup(bot : commands.Bot):
    
    await bot.add_cog(Dm(bot))
    print("Dm cog loaded.")