import discord
import wavelink
from typing import cast

class Pause(discord.ui.Button):

    def __init__(self , requester : discord.User | None):
        super().__init__(label="Pause"  , style=discord.ButtonStyle.primary)
        self.requester = requester
    async def callback(self, interaction: discord.Interaction): 
        
        player : wavelink.Player = cast(wavelink.Player , interaction.guild.voice_client)

        if not player:
            await interaction.response.send_message("I am not playing songs. Join a voice channel and listen to your favourite songs!", ephemeral=True)
            return
        if self.requester:
            if self.requester.id != interaction.user.id:
                await interaction.response.send_message("You din't play the song to pause.",ephemeral=True)
                return
        
        
        
        if player.paused:
            await interaction.response.send_message("The song has already been paused.",ephemeral=True)
            return
        
        await player.pause(True)
        
        await interaction.response.send_message(f"The Song is now paused." , ephemeral=True)


class Resume(discord.ui.Button):
    
    def __init__(self , requester : discord.User | None):
        super().__init__(label="Resume"  , style=discord.ButtonStyle.primary)
        self.requester = requester

    async def callback(self, interaction: discord.Interaction): 
        
        player : wavelink.Player = cast(wavelink.Player , interaction.guild.voice_client)

        if not player:
            await interaction.response.send_message("I am not playing songs. Join a voice channel and listen to your favourite songs!", ephemeral=True)
            return
        if self.requester:
            if self.requester.id != interaction.user.id:
                await interaction.response.send_message("You din't play the song to resume.",ephemeral=True)
                return
            
        if not player.paused:
            await interaction.response.send_message("The song has already been played.",ephemeral=True)
            return
        
        await player.pause(False)

        await interaction.response.send_message(f"The Song is now resumed." , ephemeral=True)
        
        
class Skip(discord.ui.Button):
    
    def __init__(self , requester : discord.User | None ):
        super().__init__(label="Skip"  , style=discord.ButtonStyle.red)
        self.requester = requester

    async def callback(self, interaction: discord.Interaction): 
        
        player : wavelink.Player = cast(wavelink.Player , interaction.guild.voice_client)

        if not player:
            await interaction.response.send_message("I am not playing songs. Join a voice channel and listen to your favourite songs!", ephemeral=True)
            return
        if self.requester:
            if self.requester.id != interaction.user.id:
                await interaction.response.send_message("You din't play the song to skip.",ephemeral=True)
                return
        
        current = player.current
        
        await player.skip(force=True)

        await interaction.response.send_message(f"The song `{current.title}` has been skipped.", ephemeral=True)

        