from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "𝐈𝛕ᷟ͢𝚣⃪ꙴ𐎓⃝🌺🇲𝗼𝗻𝘀𝘁𝗲𝗿❤‍🔥⃟⃚⃐ 🌿"
pic = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/a5b4f18770caacd1cdc7c.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐎𝐏 ѕραм - by 🌺🇲𝗼𝗻𝘀𝘁𝗲𝗿❤‍🔥⃟⃚⃐ 🌿"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**[🌺🇲𝗼𝗻𝘀𝘁𝗲𝗿❤‍🔥⃟⃚⃐ ](https://t.me/Moster_Bot_Store)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 
➪ **𝗠คѕƬєя:** ☆🌺🇲𝗼𝗻𝘀𝘁𝗲𝗿❤‍🔥⃟⃚⃐ ☆
➪ **𝗣ƴƬнοи ⩔єяនɨ០ɳ:** `{platform.python_version()}`
➪ **🌺🇲𝗼𝗻𝘀𝘁𝗲𝗿❤‍🔥⃟⃚⃐  ⩔єяនɨ០ɳ:** `{__version__}`
➪ **𝗣ƴяο ⩔єяនɨ០ɳ:** `{pyro_vr}`
◈ •━━━━━★✦♡✦★━━━━━• ◈
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
