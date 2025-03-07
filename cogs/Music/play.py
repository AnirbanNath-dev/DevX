from typing import cast
from discord.ext import commands
import discord
import wavelink
from bot.main import DevX

class Play(commands.Cog):
    def __init__(self, bot : DevX):
        self.bot = bot

    @commands.command()
    async def play(self, ctx: commands.Context, *, query: str = None) -> None:
        if query is None:
            embedVar = discord.Embed(
                title="Play Command Help",
                description="The `?play` command allows you to play a song in the voice channel you're currently in. To use the command, type `?play` followed by the name of the song you want to play. For example, `?play Despacito`.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embedVar)
            return

        if not ctx.guild:
            return

        player: wavelink.Player
        player = cast(wavelink.Player, ctx.voice_client)  # type: ignore

        if not player:
            try:
                player = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # type: ignore
            except AttributeError:
                await ctx.send(
                    "Please join a voice channel first before using this command."
                )
                return
            except discord.ClientException:
                await ctx.send(
                    "I was unable to join this voice channel. Please try again."
                )
                return

        player.autoplay = wavelink.AutoPlayMode.enabled
        
        # Lock the player to this channel...
        if not hasattr(player, "home"):
            player.home = ctx.channel

        tracks: wavelink.Search = await wavelink.Playable.search(query)
      
        if not tracks:
            await ctx.send(
                f"{ctx.author.mention} - Could not find any tracks with that query. Please try again."
            )
            return

        if isinstance(tracks, wavelink.Playlist):
            # tracks is a playlist...
            added: int = await player.queue.put_wait(tracks)
            await ctx.send(
                f"Added the playlist **`{tracks.name}`** ({added} songs) to the queue."
            )
        else:
            track: wavelink.Playable = tracks[0]
            await player.queue.put_wait(track)
            embedVar = discord.Embed(
                title="Added to Queue",
                description=f"`{track}` has been added to the queue."
            )
            if track.artwork:
                embedVar.set_thumbnail(url=track.artwork)
            avatar = ctx.author.avatar
            embedVar.set_footer(text=f"Requested by {ctx.author.name}" , icon_url=f"{avatar.url if avatar else "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b211152a-6401-4f44-b49f-ee7965baa89f/dgpr7mo-b0afe416-a4dd-419f-9cf5-05e32ba9aad7.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2IyMTExNTJhLTY0MDEtNGY0NC1iNDlmLWVlNzk2NWJhYTg5ZlwvZGdwcjdtby1iMGFmZTQxNi1hNGRkLTQxOWYtOWNmNS0wNWUzMmJhOWFhZDcuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.nAKsQX5faMJBGJ6-gYz_yLzI_jNZQNE8BCaKjlQiXi4"}")
            await ctx.send(embed=embedVar)
            await ctx.message.add_reaction("\u2705")
 
        if not player.playing:
            # Play now since we aren't playing anything...
            self.bot.user_playing[ctx.guild.id] = ctx.author
            await player.play(player.queue.get(), volume=30)
            

        
