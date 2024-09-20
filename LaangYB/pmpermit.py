import asyncio
from fipper import Client, filters
from fipper.enums import ChatType
from fipper.types import Message
from pyLnnggg import CMD_HELP, DEVS, tgbot
from pyLnnggg.dB.pmpermit import (
    approve_pmpermit,
    disapprove_pmpermit,
    is_pmpermit_approved,
)
from pyLnnggg.pyrogram import eor
from pyLnnggg.decorator import Laang, listen
from config import Var

from . import yins

flood = {}
OLD_MSG = {}

@listen(
    (
        filters.private
        & filters.incoming
        & ~filters.service
        & ~filters.me
        & ~filters.bot
        & ~filters.via_bot
    ),
    langs=True
)
async def pmpermit_func(client: Client, message: Message, _):
    user_ = message.from_user
    me_id = client.me.id
    pmper = Var.PMPERMIT

    if not pmper:
        return

    if user_.is_bot or user_.is_self or user_.is_contact or user_.is_verified:
        return

    if user_.is_scam:
        await message.reply_text(_['permit_1'])
        await client.block_user(user_.id)
        return

    if user_.is_support:
        return

    if await is_pmpermit_approved(me_id, user_.id):
        return

    if user_.id in DEVS:
        if not await is_pmpermit_approved(me_id, user_.id):
            await approve_pmpermit(me_id, user_.id)
            return await message.reply(_['permit_2'].format(user_.mention, user_.mention))
        else:
            return

    pm_limit = int(Var.PERMIT_LIMIT)
    limits = pm_limit + 1

    async for m in client.get_chat_history(user_.id, limit=limits):
        if m.reply_markup:
            await m.delete()

    if str(user_.id) in flood:
        flood[str(user_.id)] += 1
    else:
        flood[str(user_.id)] = 1

    if flood[str(user_.id)] > limits:
        await message.reply_text(_['permit_3'])
        if str(user_.id) in OLD_MSG:
            OLD_MSG.pop(str(user_.id))
            flood.update({user_.id: 0})
        return await client.block_user(user_.id)

    try:
        tgbot.me = await tgbot.get_me()
        results = await client.get_inline_bot_results(tgbot.me.username, f"pmpermit_{me_id}_{user_.id}")
        msg_dlt = await message.reply_inline_bot_result(
            results.query_id,
            results.results[0].id,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        msg_dlt = await client.send_message(
            user_.id,
            MSG_PERMIT,
            reply_to_message_id=yins.ReplyCheck(message),
        )

    if str(user_.id) in OLD_MSG:
        try:
            await OLD_MSG[str(user_.id)].delete()
        except Exception:
            pass

    OLD_MSG[str(user_.id)] = msg_dlt

@Laang(["ok", "a"], langs=True)
async def pm_approve(client: Client, message: Message, _):
    ids = client.me.id

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user

        if replied_user.is_self:
            await message.edit(_['permit_4'])
            return

        uid = replied_user.id

        if await is_pmpermit_approved(ids, uid):
            return await eor(message, _['permit_5'])

        await approve_pmpermit(ids, uid)
        xnxx = await eor(message, _['permit_6'])

        if str(uid) in OLD_MSG and str(uid) in flood:
            await OLD_MSG[str(uid)].delete()
            flood[str(uid)] = 0

        await asyncio.sleep(3)
        await xnxx.delete()

    else:
        aname = message.chat

        if aname.type != ChatType.PRIVATE:
            await message.edit(_['permit_7'])
            return

        uid = aname.id

        if await is_pmpermit_approved(ids, uid):
            return await eor(message, _['permit_5'])

        await approve_pmpermit(ids, uid)
        xnxx = await eor(message, _['permit_6'])

        if str(uid) in OLD_MSG and str(uid) in flood:
            try:
                await OLD_MSG[str(uid)].delete()
                flood[str(uid)] = 0
            except Exception:
                pass

        await asyncio.sleep(3)
        await xnxx.delete()

@Laang(["tolak", "da"], langs=True)
async def pm_disapprove(client: Client, message: Message, _):
    ids = client.me.id

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user

        if replied_user.is_self:
            await message.edit(_['permit_4'])
            return

        uid = replied_user.id

        if not await is_pmpermit_approved(ids, uid):
            return await eor(message, _['permit_8'])

        await disapprove_pmpermit(ids, uid)
        xnxx = await eor(message, _['permit_9'])

        await asyncio.sleep(3)
        await xnxx.delete()

    else:
        aname = message.chat

        if aname.type != ChatType.PRIVATE:
            await message.edit(_['permit_7'])
            return

        uid = aname.id

        if not await is_pmpermit_approved(ids, uid):
            return await eor(message, _['permit_8'])

        await disapprove_pmpermit(ids, uid)
        xnxx = await eor(message, _['permit_9'])

        await asyncio.sleep(3)
        await xnxx.delete()

@Laang(["block"], langs=True)
async def block_user_func(client: Client, message: Message, _):
    if not message.reply_to_message:
        return await eor(message, _['reply'])

    user_id = message.reply_to_message.from_user.id
    await eor(message, _['permit_10'])
    await client.block_user(user_id)

@Laang(["unblock"], langs=True)
async def unblock_user_func(client: Client, message: Message, _):
    if not message.reply_to_message:
        return await eor(message, _['reply'])

    user_id = message.reply_to_message.from_user.id
    await client.unblock_user(user_id)
    await eor(message, _['permit_11'])

CMD_HELP.update(
    {"pmpermit": (
        "pmpermit",
        {
            "ok": "Menerima Pesan PmPermit",
            "tolak": "Menolak Pesan PmPermit",
            "unblock [reply]": "Lepas Blokir Pengguna",
            "block [reply]": "Memblokir Pengguna",
        }
    )}
)
