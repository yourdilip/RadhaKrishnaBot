import os
from os import error
import pyrogram
from info import LOG_CHANNEL
from pyrogram import Client as Sodha
from pyrogram import filters

A = """#report....“
**Name:-** {}
**UserName:-** {}
**User ID:-** {}
**Direct link:-** {}
Else:- tg://openmessage?user_id={}„
--->
His Reported Message:- 👇👇"""

@Sodha.on_message(filters.command(["report"]))
async def report_me(bot, message):
    if message.reply_to_message:
        k = await message.reply_text("Processing...", quote=True)
        await bot.send_message(LOG_CHANNEL, A.format(message.from_user.first_name, message.from_user.username, message.from_user.id, message.from_user.mention, message.from_user.id))
        await message.reply_to_message.forward(chat_id=LOG_CHANNEL)
        await k.edit_text("Yᴏᴜʀ Rᴇǫᴜᴇsᴛ Sᴜʙᴍɪᴛᴛᴇᴅ. ❤️")
    else:
        await message.reply_text("Fɪʀsᴛ ᴡʀɪᴛᴇ ᴀ ᴍᴇssᴀɢᴇ ᴛʜᴇɴ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ.")
       
