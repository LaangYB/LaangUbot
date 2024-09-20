# Laang - Ubot
# Copyright (C) 2024 @LaangYB
#
# This file is a part of < https://github.com/LaangYB/LaangUbot >
# Please read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUbot/blob/main/LICENSE/>.
#
# FROM LaangUbot <https://github.com/LaangYB/LaangUbot>
# t.me/ybtraviss & t.me/ybtravisss

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from fipper import Client, __version__ as fip_ver
from fipper.types import Message
from platform import python_version

from pyLaang import __version__, laang_ver
from pyLaang import CMD_HELP, HOSTED_ON, tgbot
from pyLaang.decorator import Laang

from . import yins

@Laang(["alive", "yins"])
async def aliveme(client: Client, message: Message):
    try:
        tgbot.me = await tgbot.get_me()
        results = await client.get_inline_bot_results(tgbot.me.username, "alive")
        await message.reply_inline_bot_result(
            results.query_id,
            results.results[0].id,
            reply_to_message_id=yins.ReplyCheck(message),
        )
    except Exception as e:
        user = await client.get_me()
        output = (
            f"**🔗 [Laang Ubot Project](https://github.com/LaangYB/LaangUbot)**\n\n"
            f"**{var.ALIVE_TEXT}**\n\n"
            f"╭───────────◈───────────╮\n"
            f"👤 **Owner :** [{user.first_name}](tg://user?id={user.id})\n"
            f"📚 **Modules Loaded :** `{len(CMD_HELP)} Modules`\n"
            f"🐍 **Python Version :** `{python_version()}`\n"
            f"🚀 **Pyrogram Version :** `{fip_ver}`\n"
            f"🛠 **Py-Laang Version :** `{__version__}`\n"
            f"🔧 **Laang Version :** `{laang_ver}` [{HOSTED_ON}]\n"
            "╰───────────◈───────────╯\n\n"
        )
        await message.delete()
        await message.reply_text(
            text=output,
            disable_web_page_preview=True,
        )

CMD_HELP.update(
    {"alive": (
        "alive",
        {
            "alive": "Check Your Userbot.",
        }
    )}
)
