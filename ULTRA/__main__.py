import os
try:
  from LEGENDX import id, ID, devs, rd, wt
except:
  os.system("pip install LEGENDX==0.0.21")
  from LEGENDX import id, ID, devs
finally:
  print ("ULTRA X IS STARTING WITH TELETHON") 
from ULTRA import bot, CMD_HELP
from sys import argv
os.system("pip install telethon==1.19.0")
import sys
import os
from ULTRA import bot
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from ULTRA.utils import command, remove_plugin, load_module
from var import Var
from pathlib import Path
from ULTRA import LOAD_PLUG
import sys
import asyncio
import traceback
import os
import ULTRA.utils
from .data.alive_db import add_token, give_token, add_grp, get_grp, get_token
os.system("pip install google_trans_new")
import glob
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient, Button
from var import Var
from ULTRA.utils import load_module, load_pro
from ULTRA import LOAD_PLUG, BOTLOG_CHATID
from pathlib import Path
import asyncio
TOKEN = os.environ.get("TG_BOT_TOKEN", None)
import telethon.utils
try:
  from securex import en, de, ef, df
except:
  pass

i = 0
async def botsetup():
  try:
    k = await get_token()
    if k:
      return
    async with bot.conversation("botfather") as af:
      await af.send_message("/newbot")
      await af.get_response()
      await af.send_message(f'{(await bot.get_me()).username or (await bot.get_me()).id}_bot')
      await af.get_response()
      await af.send_message(f'{(await bot.get_me()).username or (await bot.get_me()).id}_Super_Bot')
      res = (await af.get_response()).text
      if res.startswith("Sorry"):
        for x in range(50):
          await af.send_message(f'{(await bot.get_me()).username or (await bot.get_me()).id}_{i}_Bot')
          i += 1
          k = (await af.get_response()).text
          if not k.startswith("Sorry"):
            break
          else:
            continue
        file = open("bot.txt", "w")
        file.write(k)
        file.close()
      else:
        file = open("bot.txt", "w")
        file.write(res)
        file.close()
      f = open("bot.txt")
      await add_token(f.readlines()[3])
      f.close()
  except Exception as e:
    print (str(e))







EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", False)
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)
ONLINE_ALERT = os.environ.get("ONLINE_ALERT")
os.system("pip install LEGENDX==0.0.21")
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

import glob



path = 'ULTRA/plugins/assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))




path = 'ULTRA/plugins/*.py'
files = glob.glob(path)
for name in files:
  with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))


async def install():
    i =0
    chat = Var.PLUGIN_CHANNEL
    documentss = await bot.get_messages(chat, None , filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await bot.download_media(await bot.get_messages(chat, ids=mxo), "ULTRA/plugins/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            print(f'{i} plugin install')
        else:
            print ("Failed")
import ULTRA._core
import os
print("UltraX is Up and Awake! ©️ TeamUltraX 2021")
async def legend():
  pro = await xbot.get_me()
  legend = await bot.get_me()
  LEGENDX = f"""
**Sᴏᴍᴇᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ ! Lᴇᴛs Cʜᴇᴄᴋ** 🤔 

`☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎`

**Dɪɴɢ Dᴏɴɢ...** `.\./.\` **Tɪɴɢ Tᴏɴɢ...** `./.\./` **UʟᴛʀᴀX Hᴀs Bᴇᴇɴ Dᴇᴘʟᴏʏᴇᴅ !!**

**Pɪɴɢ Pᴏɴɢ...**

**➥ Mᴀsᴛᴇʀ** `➪` **@{legend.username}**
**➥ Assɪsᴛᴀɴᴛ** `➪` **@{pro.username}**
**➥ Sᴜᴘᴘᴏʀᴛ** `➪` **@UltraXchaT**
**➥ Cʜᴀɴɴᴇʟ** `➪` **@UltraX_SupporT**

**Cʜᴇᴄᴋ ᴍᴏɪ Pɪɴɢ ᴛɪᴍᴇ ʙʏ** `.ping` **[Fᴏʀ UsᴇʀBᴏᴛ] or** `/ping` **[Fᴏʀ Assɪsᴛᴀɴᴛ]**
"""
  if ONLINE_ALERT:
    try:
      PROBOYX = [[Button.inline("Hᴇʀᴏᴋᴜ Vᴀʀs", data='ass_back')]]
      
      await xbot.send_message(bot.me.id, LEGENDX, buttons=PROBOYX)
    except:
       pass
  else:
      print("YOUR BOT DEPLOYED SUCCESSFULLY")

async def danger(username):
  i = 0
  xx = 0
  async for x in bot.iter_dialogs():
    if x.is_group or x.is_channel:
     try:
       await bot.edit_permissions(x.id, username, view_messages=False)
       i += 1
     except:
       xx += 1
  print(f"THE DANGER USER WAS BANNED IN {i-xx}")
bot.loop.run_until_complete(botsetup())
from ULTRAX import xbot
try:
  xbot.start(give_token())
except:
  bot.loop.run_until_complete(botsetup())
else:
  print ('Error - on Bot setup')
#bot.loop.run_until_complete(danger("")) # Temporary
bot.loop.run_until_complete(legend())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
    
else:
    bot.run_until_disconnected()
    

