import pymongo
from pymongo import MongoClient 
import discord
import os
from discord.ext import commands
import asyncio
import random
from time import sleep
from googlesearch import search
from Googlesearch import linksearch
cluster=MongoClient("id")
db = cluster["discord"]
collection = db["id"]

prefix = "!"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")
brief="hidden"
@client.event
async def on_ready():
  print("My username is " + client.user.name + " and I am running with the ID: " + str(client.user.id))
  game = discord.Game('Testing')
  await client.change_presence(status=discord.Status.idle, activity=game)
  async for guild in client.fetch_guilds(limit=150):
    print(guild.name)
#welcome message is completed no more edits required
@client.event
async def on_member_join(member):
  embed = discord.Embed(title=f' Welcome To Server Name {member}', description =
  """
  \n
  In this server we connect new and struggling black entrepreneurs to essential resources.
  \n
  These include: 

  -Investors
  -Accomplished Entrepreneurs
  -Certified financial resources
  -Business strategy resources
  -Webinars
  
  We at ResourceASK hope that you find business success through our services :)""", color=discord.Color.blue())
  await member.send(embed=embed)
  return

@client.command(name="log", brief="logs a resource", pass_context = True)
async def log(ctx):
  user = ctx.message.author
  embed = discord.Embed(name="Log a resorce", description = "Hi " +ctx.author.mention + 
  "\nIn order to log a resource please await for a private message from the ResourceASK Bot." +
  "\nPlease remember this resource has to go through a credibility check so there may be a delay in addition to the database.", color=discord.Color.blue())
  await ctx.send(embed=embed)
  embed = discord.Embed(name= "Log a resource", description = "Hi " +ctx.author.mention + 
  "\nPlease enter:"+
  """\n
  -Resource url or file link
  -Category of resource
  -Time period before expiration
  -Area Specifications
  -Gender specifications""", color= discord.Color.blue())
  await user.send(embed=embed)
  msg = await client.wait_for("message", check=lambda m: m.author == ctx.author)
  if isinstance(msg.channel, discord.channel.DMChannel):
    content=msg.content
    info= content.split(", ")
    keys =['link', 'category','expiration', 'area', 'gender']
    post = dict(zip(keys, info))
    collection.insert_one(post)
    embed = discord.Embed(title = "Log a resource", description = "Thank you for your submission.", color= discord.Color.blue())
    await user.send(embed=embed)
 
@client.command(name="databaseoutput", brief="outputs a resource from our database collection", pass_context=True)
async def databaseoutput(ctx):
  user=ctx.message.author
  desc = """Please enter some specific information relavent to the resource this includes:
        -Resource url or file link
        -Category of resource
        -Time period before expiration
        -Area Specifications
        -Gender specifications
        Wherever you may not have specifications please enter none."""
  embed = discord.Embed(title="Output a Resource", description = desc, color=discord.Color.blue())
  await user.send(embed=embed)
  content ="joajowijo;aAAEFRioajoajoAEFAa"
  while content =="joajowijo;aAAEFRioajoajoAEFAa": 
    msg = await client.wait_for("message", check=lambda m: m.author == ctx.author)
    if isinstance(msg.channel, discord.channel.DMChannel):
      embed = discord.Embed(title="Looking For Resources", description = "please be patient.", color= discord.Color.blue())
      await user.send(embed=embed)
      content=msg.content
      info = content.split(", ")
      keys =['link', 'category','expiration', 'area', 'gender']
      post = dict(zip(keys, info))
      deleted = post.copy()
      desired_value = "none"
      for value in post:
        if post[value]==desired_value:
          del deleted[value]
      results= collection.find(deleted)
      clauses=[]
      for result in results:
        clauses.append(result["link"])
      formatted = ""
      count=1
      for i in clauses:
        formatted +=str(count)+". " + i + "\n"
        count+=1
      embed = discord.Embed(title="Output a Resource from the Database", description = formatted, color=discord.Color.blue())
      await user.send(embed=embed)
    
@client.command(name="output", brief="outputs a resource", pass_context=True)
async def output(ctx):
        user=ctx.message.author
        desc = """Please enter relevant key words to the resource,  this may include:
        Type of resource 
        Time period before expiration
        Area Specifications
        Gender specifications"""
        embed = discord.Embed(title="Output a Resource", description = desc, color=discord.Color.blue())
        await ctx.send(embed=embed)
        content ="joajowijo;aAAEFRioajoajoAEFAa"
        while content =="joajowijo;aAAEFRioajoajoAEFAa": 
          msg = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
          embed = discord.Embed(title="Looking For Resources", description = "please be patient.", color= discord.Color.blue())
          await ctx.send(embed=embed)
          content=msg.content
          info = content.split(", ")
          formatted = ""
          count=1
          for i in linksearch(info):
                formatted+= str(count) + ". " + i + "\n"
                count+=1
          formatted+="All relevant links have been outputted"
          embed = discord.Embed(title="Output a Resource", description = formatted, color=discord.Color.blue())
          await ctx.send(embed=embed)
  
@client.command(name="privateoutput", brief="outputs a resource", pass_context=True)
async def output(ctx):
        user=ctx.message.author
        desc = """Please enter relevant key words to the resource,  this may include:
        Type of resource 
        Time period before expiration
        Area Specifications
        Gender specifications"""
        embed = discord.Embed(title="Output a Resource", description = desc, color=discord.Color.blue())
        await user.send(embed=embed)
        content ="joajowijo;aAAEFRioajoajoAEFAa"
        while content =="joajowijo;aAAEFRioajoajoAEFAa": 
          msg = await client.wait_for("message", check=lambda m: m.author == ctx.author)
          if isinstance(msg.channel, discord.channel.DMChannel):
            embed = discord.Embed(title="Looking For Resources", description = "please be patient.", color= discord.Color.blue())
            await user.send(embed=embed)
            content=msg.content
            info = content.split(", ")
            formatted = ""
            count=1
            for i in linksearch(info):
                  formatted+= str(count) + ". " + i + "\n"
                  count+=1
            formatted+="All relevant links have been outputted."
            embed = discord.Embed(title="Output a Resource", description = formatted, color=discord.Color.blue())
            await user.send(embed=embed)
              

@client.command(name="help", breif= "prints help menu", pass_context = True)
async def help(ctx):
  embed = discord.Embed(title = "Help", description= "Help menu", color= discord.Color.blue())
  embed.add_field(name="Prefix", value=str(prefix), inline= False)
  embed.add_field(name="Clear", value="Deletes set amount of messages", inline=False)
  embed.add_field(name="Kick", value = "Kick's a member", inline=False)
  embed.add_field(name="Ban", value = "Ban's a member", inline = False)
  embed.add_field(name="Log a resource", value="Logs a resource into the main database (use !log)", inline =False)
  embed.add_field(name="Output a resource from the database", value="Outputs a resource from the main database (use !databaseoutput)", inline=False)
  embed.add_field(name="Output a resource", value="Outputs a resource from google searches (use !output)", inline=False)
  embed.add_field(name="Privately output a resource", value="Outputs a resource from google in direct messages (use !privateoutput)", inline=False)
  await ctx.send(embed=embed)

@client.command(name ='kick', brief = "kicks a person", pass_context=True)
async def kick(ctx, member : discord.Member, *, reason = None):
  await member.kick(reason=reason)

@client.command(name = "ban", brief="bans a person", pass_context = True)
async def ban(ctx, member : discord.Member, *, reason =None):
  await member.ban(reason=reason)

@client.command(name="clear", brief= "clears messages", pass_context=True)
async def clear(ctx, amount=0):
  if amount== 0:
    embed = discord.Embed(title = "Not enough data ",description = "Please add the amount of messages you want to clear", color= discord.Color.blue())
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)
  else:
    embed = discord.Embed(title = "Clearing messages",description="clearing " + str(amount) + " messages" +ctx.author.mention, color = discord.Color.blue())
    amount+=2
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=amount)


 

client.run(os.environ['DISCORD_TOKEN'])
