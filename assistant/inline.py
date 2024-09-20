# Laang - Ubot
# Copyright (C) 2024 @LaangYB
# This file is a part of <https://github.com/LaangYB/LaangUbot>
# Please read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUbot/blob/main/LICENSE/>.
# FROM LaangUbot <https://github.com/LaangYB/LaangUbot>
# t.me/ybtraviss & t.me/ybtraviss

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
from platform import python_version
from datetime import datetime
from fipper import __version__ as fip_ver, Client
from fipper.types import *
from config import *
from pyLaang import CMD_HELP, HOSTED_ON, StartTime, __version__, laang_ver, hndlr
from pyLaang.assistant import inline
from . import *

def help_string() -> str:
    return f"""
    <b>Help Module:</b>
    <b>Prefixes:</b> <code>{hndlr}</code>
    <b>Plugin:</b> <code>{len(CMD_HELP)}</code>
    """

def update_string() -> str:
    return f'''
    <b>Tersedia Pembaruan Untuk [{branch}]</b>
    <b>•</b> Klik Update Untuk Memperbarui [{branch}]
    <b>•</b> Klik Changelog Untuk Melihat Pembaruan
    '''

def alive_string() -> str:
    return f'''
    <b>🌟 Laang UBOT 🌟</b>
    <b>{var.ALIVE_TEXT}</b>
    <b>╭━═━═━═━═━═━═━═━═━╮</b>
    💡 <b>Modules Loaded:</b> <code>{len(CMD_HELP)} Active</code>
    🐍 <b>Python Version:</b> <code>{python_version()}</code>
    🚀 <b>Pyrogram Version:</b> <code>{fip_ver}</code>
    ⚙️ <b>Py-Laang Version:</b> <code>{__version__}</code>
    🛠️ <b>Laang Version:</b> <code>{laang_ver}</code> [{HOSTED_ON}]
    <b>╰━═━═━═━═━═━═━═━═━╯</b>
    '''

@inline(pattern="help")
async def inline_result(_, inline_query: InlineQuery) -> None:
    rslts = await yins.inline_help(help_string())
    await inline_query.answer(rslts, cache_time=0)

@inline(pattern="paste", client_only=True)
async def inline_result(_, iq: InlineQuery) -> None:
    query = iq.query
    ok = query.split("-")[1]
    rslts = [
        InlineQueryResultArticle(
            title="Paste Laang Ubot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• SpaceBin •",
                            url=f"https://spaceb.in/{ok}",
                        ),
                        InlineKeyboardButton(
                            text="• Raw •",
                            url=f"https://spaceb.in/api/v1/documents/{ok}/raw",
                        ),
                    ]
                ]
            ),
            input_message_content=InputTextMessageContent("Pasted to Spacebin 🌌"),
        )
    ]
    await iq.answer(rslts, cache_time=0)

@inline(pattern="alive", client_only=True)
async def inline_result(_: Client, iq: InlineQuery) -> None:
    aliv = await yins.inline_alive(alive_string())
    await iq.answer(aliv, cache_time=0)

@inline(pattern="ping", client_only=True)
async def inline_result(_: Client, iq: InlineQuery) -> None:
    start = datetime.now()
    uptime = await yins.get_readable_time((time.time() - StartTime))
    time.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    out_ping = (
       f"<b>🌟 Laang UBot 🌟</b>\n\n"
       f"<b>💥 Respons Time:</b> <code>{duration}ms</code>\n"
       f"<b>⏱ Uptime:</b> <code>{uptime}</code>"
    )
    ping_result = [
        InlineQueryResultArticle(
            title="Ping Laang Ubot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• Help •",
                            callback_data="plugins-tab",
                        ),
                    ]
                ]
            ),
            input_message_content=InputTextMessageContent(out_ping),
        )
    ]
    await iq.answer(ping_result, cache_time=0)

@inline(pattern='in_update', client_only=True)
async def inline_update(client: Client, iq: InlineQuery) -> None:
    query = iq.query
    update_results = [
        InlineQueryResultArticle(
            title='Update Laang Ubot!',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text='• Update •',
                            callback_data='update_now',
                        ),
                        InlineKeyboardButton(
                            text='• Changelog •',
                            callback_data='changelog',
                        ),
                    ]
                ]
            ),
            input_message_content=InputTextMessageContent(update_string()),
        )
    ]
    await iq.answer(update_results, cache_time=0)

@inline(pattern='pmpermit', client_only=True)
async def inline_pmpermit(_, iq: InlineQuery) -> None:
    query = iq.query
    ids = query.split("_")[1]
    user_ids = query.split("_")[2]
    xnxx = await yins.inline_pmpermit(ids, user_ids)
    await iq.answer(xnxx, cache_time=0)

@inline(pattern='pin')
async def inline_update(client: Client, iq: InlineQuery) -> None:
    query = iq.query
    ok = query.split("_")[1]
    update_results = [
        InlineQueryResultArticle(
            title='Pinned Laang Ubot!',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text='• Cek Pinned •',
                            url=f'{ok}',
                        ),
                    ]
                ]
            ),
            input_message_content=InputTextMessageContent(f'\nPesan Berhasil di gw sematkan njing!!!'),
        )
    ]
    await iq.answer(update_results, cache_time=0)

@inline(pattern='langs', client_only=True, langs=True)
async def inline_lang(client: Client, iq: InlineQuery, _) -> None:
    text, button = await yins.inline_languages(_)
    update_results = [
        InlineQueryResultArticle(
            title='langs Laang Ubot!',
            reply_markup=InlineKeyboardMarkup(button),
            input_message_content=InputTextMessageContent(text),
        )
    ]
    await iq.answer(update_results, cache_time=0)
