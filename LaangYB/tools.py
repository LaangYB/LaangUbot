import platform
import re
import socket
import uuid
import psutil

from asyncio import gather
from os import remove
from time import sleep

from fipper import Client
from fipper.enums import ChatType
from fipper.types import Message

from pyLnnggg import Laang, CMD_HELP, OWNER_ID
from pyLnnggg.pyrogram import eor

from . import yins

OWNER_ID = '6144669103'

@Laang([".info", "chatinfo", "ginfo"])
async def chatinfo_handler(client: Client, message: Message):
    response = await eor(message, "<i>Processing...</i>")
    try:
        if len(message.command) > 1:
            chat_u = message.command[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await response.edit(
                    "Gunakan perintah ini di dalam grup atau gunakan <code>^chatinfo [group username atau id]</code>"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)

        chat_type = chat.type.replace("ChatType.", "").capitalize()
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"

        out_str = f"""
<b>❯❯ CHAT INFORMATION ❮❮</b>

🆔 <b>ID Obrolan:</b> <code>{chat.id}</code>
👥 <b>Judul:</b> {chat.title}
👤 <b>Nama Pengguna:</b> {username}
📩 <b>Jenis:</b> <code>{chat_type}</code>
🏛️ <b>ID Pusat Data:</b> <code>{dc_id}</code>
🗣️ <b>Apakah Scam:</b> <code>{chat.is_scam}</code>
🎭 <b>Apakah Palsu:</b> <code>{chat.is_fake}</code>
✅ <b>Terverifikasi:</b> <code>{chat.is_verified}</code>
🚫 <b>Dibatasi:</b> <code>{chat.is_restricted}</code>
🔰 <b>Terlindungi:</b> <code>{chat.has_protected_content}</code>
🚻 <b>Total Anggota:</b> <code>{chat.members_count}</code>
📝 <b>Deskripsi:</b>

<code>{description}</code>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                response.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=yins.ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await response.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await response.edit(f"<b>INFO:</b> <code>{e}</code>")


@Laang(["limit", "lmt"])
async def spamban(client: Client, message: Message):
    '''
    ========================×========================
            Copyright (C) 2024-present LaangYB
    ========================×========================
    '''
    msg = await eor(message, "<i>Processing...</i>")
    bot_username = "@SpamBot"
    await client.unblock_user(bot_username)
    await client.send_message(bot_username, "/start")
    sleep(1)
    async for response in client.search_messages(bot_username, limit=1):
        if response:
            await msg.edit_text(f"❯❯ Status Limit ❮❮\n\n{response.text}")


@Laang(["sys", "system"])
async def system_stats(client: Client, message: Message):
    # Pastikan hanya owner yang bisa menjalankan perintah ini
    if message.from_user.id != OWNER_ID:
        await message.reply("❌ Anda tidak memiliki izin untuk menggunakan perintah ini.")
        return

    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = yins.humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current

    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"

    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{yins.humanbytes(du.used)} / {yins.humanbytes(du.total)} ({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())

    neat_msg = f"""❯❯ <b>System Info</b> ❮❮

<b>PlatForm :</b> <code>{splatform}</code>
<b>PlatForm - Release :</b> <code>{platform_release}</code>
<b>PlatFork - Version :</b> <code>{platform_version}</code>
<b>Architecture :</b> <code>{architecture}</code>
<b>Hostname :</b> <code>{hostname}</code>
<b>IP :</b> <code>{ip_address}</code>
<b>Mac :</b> <code>{mac_address}</code>
<b>Processor :</b> <code>{processor}</code>
<b>Ram :</b> <code>{ram}</code>
<b>CPU :</b> <code>{cpu_len}</code>
<b>CPU FREQ :</b> <code>{cpu_freq}</code>
<b>DISK :</b> <code>{disk}</code>
    """
    
    await message.reply(neat_msg)


CMD_HELP.update(
    {"tools": (
        "tools",
        {
            ".info": "Dapatkan info grup dengan deskripsi lengkap.",
            "chatinfo": "Dapatkan info grup atau pengguna dengan deskripsi lengkap.",
            "id": "Dapatkan ID pengguna.",
            "limit": "Cek status limit Telegram dari @SpamBot.",
            "sys": "Gunakan ini untuk mengecek sistem Ubot Anda.",
        }
        )
    }
)
