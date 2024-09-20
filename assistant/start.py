# Laang - Ubot
# Copyright (C) 2024 @LaangYB
#
# This file is a part of <https://github.com/LaangYB/LaangUbot>
# Please read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUbot/blob/main/LICENSE/>.
#
# FROM LaangUbot <https://github.com/LaangYB/LaangUbot>
# t.me/ybtraviss & t.me/ybtraviss

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from fipper import filters
from fipper.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyLaang import __version__, tgbot
from pyLaang.assistant import callback

START = """
❏ Haii {}
╭╼┅━━━━━╍━━━━━┅━━━━━━━┅╾
├▹ {} Adalah Ubot Pyrogram Telegram
├▹ Yang Dibuat Untuk TO THE POINT 
├▹ Dan Memiliki Modul Yg Bisa Anda Gunakan
├▹ Bisa Membuat Ubot Sampai Dengan 10 String 
╰╼┅━━━━━╍━━━━━┅━━━━━━━┅╾
❏ © py-Laang v{}
"""

@tgbot.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user.mention
    buttons = [
        [InlineKeyboardButton("☞︎︎︎ Cʀᴇᴀᴛᴇ Uʙᴏᴛ ☜︎︎︎", callback_data="multi_client")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅ", callback_data="help_or_command"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
        ],
    ]
    await bot.send_message(
        msg.chat.id,
        START.format(msg.from_user.mention, mention, __version__),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@callback("help_or_command")
async def help_or_command(_, cq):
    await cq.answer("Sedang Tahap Percobaan...", show_alert=True)

@callback("about")
async def about(_, cq):
    await cq.answer("Sedang Tahap Percobaan...", show_alert=True)

@callback("multi_client")
async def multi_client(_, cq):
    button = [
        [
            InlineKeyboardButton(text="SESSION 1", callback_data="session_1"),
            InlineKeyboardButton(text="SESSION 2", callback_data="session_2"),
        ],
        [
            InlineKeyboardButton(text="SESSION 3", callback_data="session_3"),
            InlineKeyboardButton(text="SESSION 4", callback_data="session_4"),
        ],
        [InlineKeyboardButton(text="SESSION 5", callback_data="session_5")],
    ]
    await cq.message.reply(
        text="String Session Mana Yang Ingin Anda Buat ???",
        reply_markup=InlineKeyboardMarkup(button),
    )
