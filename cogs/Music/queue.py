from typing import cast
import wavelink
from discord.ext import commands
import discord

class Queue(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command()
    async def queue(self, ctx: commands.Context) -> None:
        
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            await ctx.send(embed=discord.Embed(description="I'm currently not playing any song. Please add a song to the queue first."))
            return

        embed = discord.Embed(
            color=0xe882ff,
        )
        embed.add_field(name="<a:music_disc:1347098774203269142> Now Playing" , value=f"[`{player.current.title}`]({player.current.uri})" , inline=False)
        count = player.queue.count
        if player.current.artwork:
            embed.set_thumbnail(url=player.current.artwork)
        if count > 0:
            embed.add_field(
                name="<:cmusic:1346851234082197584> Upcoming Songs:",
                value="\n".join([f"**{i+1}.** `{track.title}` by `{track.author}`" for i, track in enumerate(player.queue)]),
                inline=False
            )
        else:
            embed.add_field(
                name="Queue is Empty!",
                value="There are no upcoming songs in the queue.",
                inline=False
            )
            
        avatar = ctx.author.avatar
        
        embed.set_footer(text=f"Requested by {ctx.author.name}" , icon_url=f"{avatar.url if avatar else "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b211152a-6401-4f44-b49f-ee7965baa89f/dgpr7mo-b0afe416-a4dd-419f-9cf5-05e32ba9aad7.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2IyMTExNTJhLTY0MDEtNGY0NC1iNDlmLWVlNzk2NWJhYTg5ZlwvZGdwcjdtby1iMGFmZTQxNi1hNGRkLTQxOWYtOWNmNS0wNWUzMmJhOWFhZDcuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.nAKsQX5faMJBGJ6-gYz_yLzI_jNZQNE8BCaKjlQiXi4"}")
        
        await ctx.send(embed=embed)

