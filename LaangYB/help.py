from fipper import Client
from fipper.types import Message
from random import choice
from time import sleep

from pyLnnggg import Laang, CMD_HELP, tgbot
from pyLnnggg.pyrogram import eod, eor

from . import hndlr, yins

@Laang(["inline", "help"], langs=True)
async def module_help(client: Client, message: Message, _):
    args = yins.get_cmd(message)
    
    if args:
        if args in CMD_HELP:
            plugs = await yins.PluginXd(CMD_HELP, args)
            cmd_string = (
                f"<b>PLUGIN:</b> {args.capitalize()}\n"
                f"<b>HNDLR:</b> <code>{choice(hndlr)}</code>\n\n" + "".join(plugs)
            )
            await eor(message, cmd_string)
        else:
            await eod(message, _['help_1'].format(args, choice(hndlr)))
    else:
        try:
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, "help")
            await message.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=yins.ReplyCheck(message),
            )
        except Exception as e:
            user = await client.get_me()
            string = ""
            for i in CMD_HELP:
                string += "`" + str(i) + "`\t\t\t**⍟**\t\t\t"
            xnxx = await eor(message, "🤖")
            sleep(3)
            await xnxx.edit(
                f"**[✦ Laang Ubot ✦](https://github.com/LaangYB/LaangUbot)**\n"
                f"**🚀 Total Plugins:** `{len(CMD_HELP)}` **Modules Loaded**\n"
                f"**👑 Owner:** [{user.first_name}](tg://user?id={user.id})\n\n"
                f"**🔹**   {string}\n"
                f"{_['help_2']}"
            )
