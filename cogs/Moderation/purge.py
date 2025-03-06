from discord.ext import commands
import asyncio

class Purge(commands.Cog):
    
    def __init__(self , bot : commands.Bot):
        super().__init__()
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self , ctx : commands.Context , count : int):
        
        await ctx.channel.purge(limit=count+1)
        msg = await ctx.send(f"{count} message(s) are deleted succesfully")
        await asyncio.sleep(5)
        await msg.delete()
        

async def setup(bot : commands.Bot):
    
    await bot.add_cog(Purge(bot))
    print("Purge cog loaded.")