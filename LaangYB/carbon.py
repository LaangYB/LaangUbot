import os

from fipper import Client
from fipper.types import Message

from pyLaang import Laang, CMD_HELP
from pyLaang.pyrogram import eod, eor

from . import *

@Laang(["carbon"], langs=True)
async def carbon_func(client: Client, msg: Message, _):
    if not msg.reply_to_message or yins.get_cmd(msg):
        return await eod(msg, _["reply"])
    
    reply_msg = msg.reply_to_message
    if reply_msg:
        if reply_msg.media:
            b = await client.download_media(reply_msg)
            with open(b, "r") as a:
                code = a.read()
            os.remove(b)
        else:
            code = reply_msg.text
    else:
        code = yins.get_cmd(msg)
    
    m = await eor(msg, _["carbon_1"])
    carbon = await yins.Carbon(code=code, file_name="carbon_Laang", backgroundColor="Grey")
    await m.edit(_["upload"])
    
    try:
        await msg.client.send_photo(
            chat_id=msg.chat.id,
            photo=carbon,
            caption=_["carbon_2"].format(client.me.mention),
        )
    except Exception as e:
        await eod(m, _["err"].format(e))

CMD_HELP.update(
    {"carbon": (
        "carbon",
        {
            "carbon <reply/teks>": "Carbonised Teks",
        }
    )}
)
