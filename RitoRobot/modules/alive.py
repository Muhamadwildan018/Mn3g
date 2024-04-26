from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from RitoRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot, OWNER_USERNAME


@pbot.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT += f"┏━━━━━━━━━━━━━━━━━━━━┓\n\n"
    TEXT += f"┠➣ **๏ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ʙʏ:** [ᴡɪʟᴅᴀɴ](tg://user?id=5779185981)` \n"
    TEXT += f"┠➣ **๏ ғᴏᴜɴᴅᴇʀ :** [ᴡɪʟᴅᴀɴ] (https://t.me/mhmdwldnnnn)` \n"
    TEXT += f"┠➣ **๏ ꜱᴜᴘᴘᴏʀᴛ :** [sᴛᴏʀᴇ](https://t.me/Disney_storeDan)` \n"
    TEXT += f"┗━━━━━━━━━━━━━━━━━━━━┛\n\n"
    TEXT += "**ᴛᴇʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴜ ᴅɪsɪɴɪ ❤️**"
    BUTTON = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/musik_supportDan"),
        ],
        [
            InlineKeyboardButton("ᴍʏ ᴏᴡɴᴇʀ", url=f"t.me/mhmdwldnnnn"),
        ]
    ]
    await message.reply_photo(
        photo=f"https://telegra.ph//file/5f47ba158a30ce7d161ea.jpg",
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )
