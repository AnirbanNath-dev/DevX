from discord.ext import commands
from discord import app_commands
import discord

class ErrorHandler(commands.Cog):
    
    def __init__(self , bot : commands.Bot):
        super().__init__()
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error
    
    async def on_app_command_error(self , interaction : discord.Interaction , error : app_commands.AppCommandError):
        
        if isinstance(error , commands.BotMissingPermissions):
            await interaction.response.send_message(f"" , ephemeral=True)
        elif isinstance(error , commands.NotOwner):
            await interaction.response.send_message(f"" , ephemeral=True)
        elif isinstance(error , commands.MissingPermissions):
            await interaction.response.send_message(f"" , ephemeral=True)

        
        else:
            raise error
        
    @commands.Cog.listener()
    async def on_command_error(self ,ctx : commands.Context , error : commands.CommandError):
        
        if isinstance(error , commands.BotMissingPermissions):
            await ctx.send(f"I don't have required permissions to {ctx.command}")
        elif isinstance(error , commands.NotOwner):
            await ctx.send("Hmm , You looks suspicious for a reason!")
        elif isinstance(error , commands.MissingPermissions):
            await ctx.send("You don't have required permissions to execute the command!")
        elif isinstance(error , commands.MissingRequiredArgument):
            pass
        elif isinstance(error , commands.CommandNotFound):
            await ctx.send("Invalid command. Type `?help` to get commands")
        else:
            raise error

async def setup(bot : commands.Bot):
    
    await bot.add_cog(ErrorHandler(bot))
    print("ErrorHandler cog loaded.")
