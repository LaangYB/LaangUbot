from fipper import Client
from fipper.errors import PeerIdInvalid
from fipper.types import Message

from pyLnnggg import Laang, CMD_HELP
from pyLnnggg.pyrogram import eod, eor

from . import *

@Laang(["whois", "info"], langs=True)
async def check_user(client: Client, msg: Message, _):
    xx = await eor(msg, _['p'])
    try:
        # Extracting the user identifier from the message text
        if ' ' in msg.text:
            users = msg.text.split(" ", 1)[1]
        else:
            return await eod(xx, _["err_user"])

        try:
            target = await client.get_users(users)
        except PeerIdInvalid:
            return await eod(xx, _["err_user"])

        # Constructing the user information string
        name = f"{target.first_name} {target.last_name}" if target.last_name else target.first_name
        uname = f"@{target.username}" if target.username else "⊗"
        out_str = (
            f"""
**⇒ Informasi Pengguna ⇐**

**Name:** `{name}`
**Username:** {uname}
**User ID:** `{target.id}`
**User Prem:** `{target.is_premium}`
**Profil:** [{name}](tg://user?id={target.id})
"""
        )
        await xx.edit(out_str)
    except Exception as ex:
        return await eod(xx, str(ex))

# Updating CMD_HELP with the new information command
CMD_HELP.update(
    {"info": (
        "info",
        {
            "info <id/username>": "Dapatkan Informasi Pengguna.",
        }
    )}
)

