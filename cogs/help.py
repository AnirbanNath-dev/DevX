from discord.ext import commands
from discord import Embed , Color

class Help(commands.Cog):
    
    def __init__(self , bot : commands.Bot):
        super().__init__()
        self.bot = bot
    
        
    @commands.command(name="help" , brief="Shows a help message")
    async def help(self , ctx : commands.Context):
        
        embed = Embed(
            title="DevX Bot Help",
            color=Color.blue(),
            description="This is "
            )
        

