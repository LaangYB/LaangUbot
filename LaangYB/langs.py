from fipper import Client
from fipper.types import Message

from pyLnnggg import Laang, CMD_HELP
from pyLnnggg.Clients.client import tgbot

from . import yins

@Laang(["lang"], langs=True)
async def set_lang(client: Client, message: Message, _):
    try:
        # Retrieve the bot's own user information
        tgbot.me = await tgbot.get_me()
        
        # Fetch inline results from the bot
        results = await client.get_inline_bot_results(
            tgbot.me.username,
            f"langs_{client.me.id}"
        )
        
        # Reply with inline bot results
        await message.reply_inline_bot_result(
            results.query_id,
            results.results[0].id,
            reply_to_message_id=yins.ReplyCheck(message)
        )
    except Exception as e:
        # Handle any exceptions that occur
        await message.reply(_["err"].format(e))

# Updating CMD_HELP with the new command
CMD_HELP.update(
    {"langs": (
        "langs",
        {
            "lang": "Pilih bahasa yang ingin anda gunakan.",
        }
    )}
)
