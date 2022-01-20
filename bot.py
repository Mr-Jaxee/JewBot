import discord
from discord_components import *
from utils.file_methods import Db, Save
from discord.ext import commands
import keep_alive
keep_alive.keep_alive()

bot = commands.Bot(command_prefix='>')
bot.remove_command('help')
@bot.event
async def on_ready():
    print("Бот запустился без багов! Кошерно!")
    DiscordComponents(bot)
    while True:
          await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Hava Nagila"))


@bot.command(aliases=['рейтинг'])
async def rating(ctx, ball: str, member: discord.Member):
    if ctx.author.id == 812042950837010463:
        db = Db(member.id)
        if ball[0] == '+':
            db[str(member.id)]['Шаббат'] += int(ball[1:])
            await ctx.send(embed = discord.Embed(description = f'Моссад гордится вами, {member.mention}! Таки кошерно, {ball} шаббата!'))
        if ball[0] == '-':
            db[str(member.id)]['Шаббат'] -= int(ball[1:])
            await ctx.send(embed = discord.Embed(description = f'Нетаньяху разочарован, {member.mention}! Ой-вей, {ball} шаббата.'))
        Save(db)
    else:
        await ctx.send('У тебя нет прав')


@bot.command(aliases=['паспорт'])
async def passport(ctx, member: discord.Member = None):
    if member is None:
        db = Db(ctx.author.id)
        await ctx.send(embed = discord.Embed(description = f'Паспорт гражданина {ctx.author.mention}\nГражданство: :flag_il: \nШаббат: {db[str(ctx.author.id)]["Шаббат"]}'))
    else:
        db = Db(member.id)
        await ctx.send(embed = discord.Embed(description = f'Паспорт гражданина {member.mention}\nГражданство: :flag_il: \nШаббат: {db[str(member.id)]["Шаббат"]}'))

@bot.event
async def on_message(message):
    if "Шалом" in message.content.split():
        if message.author == bot.user:
            return
        else:
            await message.channel.send(f'Шалом, {message.author.mention}')
    if message.author == bot.user:
            return
    db = Db(message.author.id)
    async def add_exp(exp):
        db[str(message.author.id)]['Опыт'] += exp
    async def add_lvl():
        exp = db[str(message.author.id)]['Опыт']
        lvl = db[str(message.author.id)]['Шаббат']
        if exp > lvl:
            await message.channel.send(embed = discord.Embed(description = f'Моссад гордится вами, {message.author.mention}! Таки кошерно, 3 шаббата!'))
            db[str(message.author.id)]['Опыт'] = 0
            db[str(message.author.id)]['Шаббат'] += 3
    await add_exp(0.1)
    await add_lvl()
    Save(db)
    await bot.process_commands(message)

@bot.command(aliases=['хелп', 'помощь'])
async def help(ctx):
    emb = discord.Embed(title = 'Список комманд')
    emb.add_field(name='Паспорт', value = 'Показывает ваш или не ваш паспорт')
    await ctx.send(embed = emb)

bot.run('TOKEN')
