from fipper import Client
from fipper.types import Message
from pyLaang import CMD_HELP, tgbot
from pyLaang.decorator import Laang
from pyLaang.pyrogram import eod

from . import yins

@Laang(["ping"], langs=True)
async def pingme(client: Client, message: Message, _):
    if tgbot:
        try:
            xnxx = await message.reply("<b>✧</b>")
            await xnxx.edit("<b>✧✧</b>")
            await xnxx.edit("<b>✧✧✧</b>")
            await xnxx.edit("<b>✧✧✧✧</b>")
            await xnxx.edit("<b>✧✧✧✧✧</b>")
            
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, "ping")
            
            await message.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=yins.ReplyCheck(message),
            )
            await xnxx.delete()
        except Exception as e:
            if 'xnxx' in locals():
                await eod(xnxx, _['err'].format(e))

CMD_HELP.update(
    {"ping": (
        "ping",
        {
            "ping": "Check Ping Your Bot.",
        }
    )}
)
