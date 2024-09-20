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

import asyncio

from fipper import Client, enums
from fipper.errors import FloodWait
from fipper.types import Message

from pyLnnggg import Laang, CMD_HELP, DEVS, GCAST_BLACKLIST
from pyLnnggg.dB.blacklistgcast import add_blacklist_gcast, blacklisted, is_blacklist_gcast, remove_blacklist_gcast

from . import yins


@Laang([".gcast", "fw_cast"], langs=True)
async def gcast_cmd(client: Client, message: Message, _):
    '''
    ========================×========================
            Copyright (C) 2024-present LaangYB
    ========================×========================
    '''
    BL = await blacklisted()
    if message.reply_to_message:
        LaangYB = await message.reply(_["p"])
    else:
        return await message.edit_text(_["reply"])
    x = message.reply_to_message.id
    y = message.chat.id
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [
                enums.ChatType.GROUP,
                enums.ChatType.SUPERGROUP]:
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST and chat not in BL:
                try:
                    await client.forward_messages(chat, y, x)
                    done += 1
                except FloodWait as e:
                    f_t = int(e.value)
                    if f_t > 200:
                        continue
                    await asyncio.sleep(f_t)
                    await client.forward_messages(chat, y, x)
                    done += 1
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await LaangYB.edit_text(_["gcast_1"].format(done, error))


@Laang(["gcast", "broadcast"], langs=True)
async def broadcast_cmd(client: Client, message: Message, _):
    '''
    ========================×========================
            Copyright (C) 2024-present LaangYB
    ========================×========================
    '''
    BL = await blacklisted()
    if message.reply_to_message:
        LaangYB = await message.reply(_['p'])
    else:
        return await message.edit_text(_['reply'])
    x = message.reply_to_message.id
    y = message.chat.id
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in [
                enums.ChatType.GROUP,
                enums.ChatType.SUPERGROUP]:
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST and chat not in BL:
                try:
                    await client.copy_message(chat, y, x)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as e:
                    f_t = int(e.value)
                    if f_t > 200:
                        continue
                    await asyncio.sleep(f_t)
                    await client.copy_message(chat, y, x)
                    done += 1
                except BaseException:
                    error += 1
    await LaangYB.edit_text(_['gcast_2'].format(done, error))


@Laang([".ucast"], langs=True)
async def ucast_cmd(client: Client, message: Message, _):
    '''
    ========================×========================
            Copyright (C) 2024-present LaangYB
    ========================×========================
    '''
    if message.reply_to_message:
        YB = await message.reply(_['p'])
    else:
        return await message.edit_text(_['reply'])

    done = 0
    error = 0

    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            chat_id = dialog.chat.id
            if chat_id not in DEVS:
                try:
                    if message.reply_to_message:
                        msg = message.reply_to_message
                        await msg.copy(chat_id)
                    elif yins.get_cmd(message):
                        cmd_msg = yins.get_cmd(message)
                        await client.send_message(chat_id, cmd_msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    
    await YB.edit_text(_['gcast_3'].format(done, error))


@Laang(['addblacklist', 'addbl'], langs=True)
async def add_bl(client: Client, message: Message, _):
    '''
    ========================×========================
            Copyright (C) 2024-present LaangYB
    ========================×========================
    '''
    chat_id = message.chat.id
    cmd = yins.get_cmd(message)
    if cmd:
        try:
            chat_ids = await client.get_chat(cmd)
            is_done = await is_blacklist_gcast(chat_ids.id)
            if not is_done:
                await add_blacklist_gcast(chat_ids.id)
                return await message.reply(_['gcast_4'].format(chat_ids.id))
            else:
                return await message.reply(_['gcast_5'].format(chat_ids.id))
        except Exception as e:
            return await message.reply(_['err'].format(e))
    else:
        is_done = await is_blacklist_gcast(chat_id)
        if not is_done:
            await add_blacklist_gcast(chat_id)
            return await message.reply(_['gcast_4'].format(chat_id))
        else:
            return await message.reply(_['gcast_5'].format(chat_id))


@Laang(['delblacklist', 'delbl'], langs=True)
async def del_bl(client: Client, message: Message, _):
    '''
    ========================×========================
            Copyright (C) 2024-present LaangYB
    ========================×========================
    '''
    chat_id = message.chat.id
    cmd = yins.get_cmd(message)
    if cmd:
        try:
            chat_ids = await client.get_chat(cmd)
            is_done = await is_blacklist_gcast(chat_ids.id)
            if is_done:
                await remove_blacklist_gcast(chat_ids.id)
                return await message.reply(_['gcast_6'].format(chat_ids.id))
            else:
                return await message.reply(_['gcast_7'].format(chat_ids.id))
        except Exception as e:
            return await message.reply(_['err'].format(e))
    else:
        is_done = await is_blacklist_gcast(chat_id)
        if is_done:
            await remove_blacklist_gcast(chat_id)
            return await message.reply(_['gcast_6'].format(chat_id))
        else:
            return await message.reply(_['gcast_7'].format(chat_id))


@Laang(['blacklist', 'blchat'], langs=True)
async def list_bl(client: Client, message: Message, _):
    '''
    ========================×========================
            Copyright (C) 2024-present LaangYB
    ========================×========================
    '''
    chats = await blacklisted()
    chat_id = f'{chats}'
    list_str = (
        chat_id.replace("[", "")
        .replace("]", "")
        .replace(",", "\n⇒ ")
    )
    count = len(chats)
    if count == 0:
        return await message.reply(_['gcast_8'])
    return await message.reply(_['gcast_9'].format(count, list_str))


CMD_HELP.update(
    {"gcast": (
        "gcast",
        {
            "fgcast [reply]": "Forward Broadcast messages in group chats.",
            "gcast [reply]": "Broadcast messages in group chats.",
            ".ucast [reply]": "Broadcast messages to users.",
            "addbl": "Add chat ID to blacklist for broadcast. Use group ID or username.",
            "delbl": "Remove chat ID from blacklist for broadcast. Use group ID or username.",
            "blchat": "View list of blacklisted chat IDs.",
        }
    )
    }
)
