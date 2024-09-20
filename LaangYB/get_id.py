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

from fipper import Client
from fipper.errors import PeerIdInvalid
from fipper.types import Message

from pyLaang import Laang
from pyLaang.pyrogram import eod, eor

from . import yins


@Laang(['id', 'get_id'], langs=True)
async def get_id(client: Client, msg: Message, _):
    usr_text = ''
    xxx = await eor(msg, _['p'])
    reply = msg.reply_to_message
    chats = msg.chat.id
    cmd = yins.get_cmd(msg)
    
    if reply:
        if reply.from_user:
            mention = reply.from_user.mention
            ids = reply.from_user.id
            usr_text += f'**User:** {mention}\n'
            usr_text += f'**ID:** {ids}\n\n'
        else:
            mention = reply.forward_from.mention
            ids = reply.forward_from.id
            usr_text += f'**User:** {mention}\n'
            usr_text += f'**ID:** {ids}\n\n'
        usr_text += f'**Get ID By {client.me.username}**'
        await xxx.edit(usr_text)
    elif cmd:
        try:
            user = await client.get_users(cmd)
        except PeerIdInvalid:
            await eod(xxx, _['err_user'])
            return
        mention = user.mention
        ids = user.id
        usr_text += f'**User:** {mention}\n'
        usr_text += f'**ID:** {ids}\n\n'
        usr_text += f'**Get ID By {client.me.username}**'
        await xxx.edit(usr_text)
    else:
        await xxx.edit(f'**ID:** {chats}')
