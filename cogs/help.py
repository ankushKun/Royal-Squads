import discord
from discord.ext import commands

dsc="""
prefix : **rs!**

`command [aliases] (optional arguments) <required arguments>`
`squad [sqd] <squad name>` - display list of squads, show members of a squad.

For admins/weeb council:
`create <leader> <squad name>` - create a new squad with the mentioned user as its leader.
`delete <squad name>` - delete a squad.
`add <member> <squad name>` - add a member to a squad.
`remove <member> <squad name>` - remove a member from a squad.

"""

class Help(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command()
  async def help(self,ctx):
    emb=discord.Embed(title="HELP",description=dsc)
    emb.set_footer(text=str(ctx.author))
    await ctx.send(embed=emb)
    
  @commands.Cog.listener()
  async def on_message(self,message):
    if message.content.lower().startswith("rs! ") and not message.author.bot:
      message.content="rs!"+message.content[4:]
      await self.bot.process_commands(message)
    
    
    
  
def setup(bot):
  bot.add_cog(Help(bot))
  print("COG : HELP LOADED")
