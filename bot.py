import discord
from discord.ext import commands
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def PesetasAEuros(ctx, pesetas:int):
    
        await ctx.send(f"{round(pesetas/166,2)} Euros")
 
@PesetasAEuros.error
async def PesetasAEuros_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.BadArgument):
            await ctx.send(f'Error ❌')
        
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications