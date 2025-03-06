import discord
import wavelink
from discord.ext import commands

class Pause(discord.ui.Button):

    def __init__(self):
        super().__init__(label="Pause"  , style=discord.ButtonStyle.primary)
        
    async def callback(self, interaction: discord.Interaction): 
        
        await interaction.response.send_message("On development" , ephemeral=True)

class Resume(discord.ui.Button):
    
    def __init__(self):
        super().__init__(label="Resume"  , style=discord.ButtonStyle.primary)
        

    async def callback(self, interaction: discord.Interaction): 
        
        
        await interaction.response.send_message("On development" , ephemeral=True)
        
        
class Skip(discord.ui.Button):
    
    def __init__(self):
        super().__init__(label="Skip"  , style=discord.ButtonStyle.red)
        

    async def callback(self, interaction: discord.Interaction): 
        
        
        await interaction.response.send_message("On development" , ephemeral=True)
        