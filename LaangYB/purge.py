from fipper import Client
from fipper.types import Message
from pyLnnggg import Laang, CMD_HELP
from pyLnnggg.pyrogram import eod, eor
from . import yins

@Laang(["purge"], langs=True)
async def purges(client: Client, msg: Message, _):
    xx = await eor(msg, _["p"])
    if await yins.CheckAdmin(client, msg):
        msg_ids = []
        count_del = 0
        
        if msg.reply_to_message:
            start_id = msg.reply_to_message.id
            end_id = msg.id

            # Create a list of message IDs to delete
            msg_ids = list(range(start_id, end_id + 1))

            # Delete messages in chunks of 100
            for chunk in [msg_ids[i:i + 100] for i in range(0, len(msg_ids), 100)]:
                await client.delete_messages(
                    chat_id=msg.chat.id, message_ids=chunk, revoke=True
                )
                count_del += len(chunk)

        return await xx.edit(_['purge'].format(count_del))
    else:
        return await eod(msg, _["admin_5"])

CMD_HELP.update(
    {"purge": (
        "purge",
        {
            "purge <reply>": "Balas ke pesan yg ingin di hapus sekaligus."
        }
    )}
)
