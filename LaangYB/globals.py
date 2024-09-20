from fipper import Client, filters
from fipper.types import Message
from pyLnnggg import Laang, CMD_HELP, OWNER_ID
from pyLnnggg.pyrogram import eor
from pyLnnggg.dB.gban import add_gbanned, gbanned_users, is_gbanned, remove_gbanned
from pyLnnggg.decorator import listen

from . import yins

OWNER_ID = 6144669103  # Note: Use integer for IDs instead of strings

@Laang([".gban"], devs=True)
async def gban_user(client: Client, message: Message, _):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ Anda tidak memiliki izin untuk menggunakan perintah ini.")

    user_id, reason = await yins.extract_user_and_reason(message, sender_chat=True)
    Laang_reply = await message.reply(_['p'])

    if not user_id:
        return await Laang_reply.edit(_['err_user'])
    if user_id == client.me.id:
        return await Laang_reply.edit(_['gban_1'])
    
    try:
        user = await client.get_users(user_id)
    except Exception:
        return await Laang_reply.edit(_['err_user'])

    if await is_gbanned(user.id):
        return await Laang_reply.edit(_['gban_2'].format(user.mention))
    
    f_chats = await yins.get_ub_chats(client)
    if not f_chats:
        return await Laang_reply.edit(_['gban_3'])

    done, er = 0, 0
    for chat_id in f_chats:
        try:
            await client.ban_chat_member(chat_id=chat_id, user_id=user.id)
            done += 1
        except BaseException:
            er += 1
    
    await add_gbanned(user.id)

    msg = _['gban_4'].format(user.mention, user.id)
    if reason:
        msg += _['admin_4'].format(reason)
    msg += _['gban_5'].format(done)
    
    await Laang_reply.edit(msg)


@Laang([".ungban"], devs=True)
async def ungban_user(client: Client, message: Message, _):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ Anda tidak memiliki izin untuk menggunakan perintah ini.")

    user_id, reason = await yins.extract_user_and_reason(message, sender_chat=True)
    Laang_reply = await message.reply(_['p'])

    if not user_id:
        return await Laang_reply.edit(_['err_user'])
    
    try:
        user = await client.get_users(user_id)
    except Exception:
        return await Laang_reply.edit(_['err_user'])

    if not await is_gbanned(user.id):
        return await Laang_reply.edit(_['gban_6'])

    ung_chats = await yins.get_ub_chats(client)
    if not ung_chats:
        return await Laang_reply.edit(_['gban_3'])

    done, er = 0, 0
    for chat_id in ung_chats:
        try:
            await client.unban_chat_member(chat_id=chat_id, user_id=user.id)
            done += 1
        except BaseException:
            er += 1

    await remove_gbanned(user.id)

    msg = _['gban_7'].format(user.mention, user.id)
    if reason:
        msg += _['admin_4'].format(reason)
    msg += _['gban_5'].format(done)
    
    await Laang_reply.edit(msg)


@Laang(["listgban"], devs=True)
async def gbanlist(client: Client, message: Message, _):
    users = await gbanned_users()
    Laang_reply = await eor(message, _['p'])
    
    if not users:
        return await Laang_reply.edit(_['gban_8'])
    
    user_list = '\n'.join([f"{idx + 1}. {user_id}" for idx, user_id in enumerate(users)])
    await Laang_reply.edit(_['gban_9'].format(user_list))


@listen(filters.incoming & filters.group)
async def globals_check(client: Client, message: Message):
    if not message.from_user:
        return
    
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    if await is_gbanned(user_id):
        try:
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass
    
    message.continue_propagation()


CMD_HELP.update(
    {"globals": (
        "globals",
        {
            "gban <reply/username/userid>": "Melakukan Global Banned ke semua grup di mana Anda sebagai admin.",
            "ungban <reply/username/userid>": "Membatalkan Global Banned.",
            "listgban": "Menampilkan daftar pengguna yang di-ban secara global.",
        }
    )}
)
