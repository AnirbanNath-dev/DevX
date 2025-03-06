from wavelink import (
    Player,
    Playable,
    TrackStartEventPayload
)

import discord
from math import floor
from bot.utils.buttons import (
    Pause,
    Resume,
    Skip
)

class MusicPlayer():
    
    def __init__(self):
        self.previous_now_playing_message : discord.Message = None

    
    async def track_start(self , payload : TrackStartEventPayload) -> None:
        player : Player | None = payload.player
        
        if not player:
            return

        track : Playable = payload.track
        track_length_ms = int(track.length)
        mins = track_length_ms // 60000  
        secs = (track_length_ms % 60000) // 1000 

        embed = discord.Embed(
            title="<a:music_disc:1347098774203269142> Now Playing" , 
            color=discord.Color.green()
        )

        embed.add_field(name="Song" , value=f"[`{track.title}`]({track.uri})" , inline=True)
        embed.add_field(name="Artist" , value=f"`{track.author}`", inline=True)
        embed.add_field(name="Duration" , value=f"`{floor(mins) if mins>=10 else f"0{floor(mins)}"}:{floor(secs) if secs>=10 else f"0{floor(secs)}"}`" , inline=True)
        if track.artwork:
            embed.set_thumbnail(url=track.artwork)

        pause = Pause()
        resume = Resume()
        skip = Skip()

        views = discord.ui.View()
        views.add_item(pause)
        views.add_item(resume)
        views.add_item(skip)
        
        if self.previous_now_playing_message:
            try:
                await self.previous_now_playing_message.delete()
            except discord.NotFound:
                pass 

        self.previous_now_playing_message = await player.home.send(embed=embed, view=views)
        
    async def track_end(self) -> None:
        
        if self.previous_now_playing_message:
            try:
                await self.previous_now_playing_message.delete()
                
            except discord.NotFound:
                pass
        
        
        
