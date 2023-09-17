from SpamX.config import *
from SpamX.core.version import version
from SpamX import sudoser, RiZoeL 
from RiZoeLX import version as pip_vr
from pyrogram import version as pyro_vr
import platform

version = version


ping_msg = PING_MSG if PING_MSG else "⚡🇩𝜩Ⓐ︎🇩 ⚡"
pic = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/f4e84fef88c1c848c138f.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐎𝐏 ѕραм - by ⚡🇩𝜩Ⓐ︎🇩 ⚡"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**[⚡🇩𝜩Ⓐ︎🇩 ⚡](https://t.me/DAEDX_HELP)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 
➪ 𝗠คѕƬєя: ☆⚡🇩𝜩Ⓐ︎🇩 ⚡☆
➪ 𝗣ƴƬнοи ⩔єяនɨ០ɳ: {platform.python_version()}
➪ ⚡🇩𝜩Ⓐ︎🇩 ⚡ ⩔єяនɨ០ɳ: {version}
➪ 𝗣ƴяο ⩔єяនɨ០ɳ: {pyro_vr}
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
