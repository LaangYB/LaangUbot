from fipper import filters
from fipper.types import Message

from pyLnnggg import Laang, CMD_HELP, listen
from pyLnnggg.dB.logdb import (
    add_grup_off, add_grup_on, add_pm_off, add_pm_on,
    is_grup_logs, is_pm_logs
)

from . import yins

PMLOG = 1
GRUPLOG = 1

@Laang(["log"], langs=True)
async def pmlogs(client: Client, message: Message, _):
    try:
        command = message.command[1]
        arg = message.text.split(None, 2)[2]
    except IndexError:
        await message.reply(_["log_1"])
        return

    if command == "pm":
        if arg == "off":
            await add_pm_off(PMLOG)
            await message.reply(_['log_2'])
        elif arg == "on":
            await add_pm_on(PMLOG)
            await message.reply(_['log_3'])
    elif command == "gc":
        if arg == "off":
            await add_grup_off(GRUPLOG)
            await message.reply(_['log_4'])
        elif arg == "on":
            await add_grup_on(GRUPLOG)
            await message.reply(_['log_5'])
    elif command == "all":
        if arg == "off":
            await add_grup_off(GRUPLOG)
            await add_pm_off(PMLOG)
            await message.reply(_['log_6'])
        elif arg == "on":
            await add_grup_on(GRUPLOG)
            await add_pm_on(PMLOG)
            await message.reply(_['log_7'])
    else:
        await message.reply(_['log_8'])

@listen(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
)
async def pmlogchat(client: Client, message: Message):
    if await is_pm_logs(PMLOG):
        chat = message.chat.id
        async for pepek in client.search_messages(chat, limit=1):
            await yins.logger_bot(client=client, pepek=pepek)

@listen(
    filters.mentioned
    & filters.incoming
    & filters.group
)
async def grouplogchat(client: Client, message: Message):
    if await is_grup_logs(GRUPLOG):
        await yins.logger_bot(client, message, True)

CMD_HELP.update(
    {"log": (
        "log",
        {
            "log [pm/gc/all] [on/off]": "Aktifkan atau matikan log untuk userbot.\n\n"
                                        "Catatan:\n"
                                        "pm: Pesan Pribadi\n"
                                        "gc: Grup Chat\n"
                                        "all: Grup Chat dan Pesan Pribadi\n\n"
                                        "Contoh:\n"
                                        ".log pm on/off",
        }
    )}
)
