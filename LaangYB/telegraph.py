import os

from fipper import Client
from fipper.types import Message
from telegraph import Telegraph, exceptions, upload_file

from pyLnnggg import Laang, CMD_HELP

from . import yins

telegraph = Telegraph()
r = telegraph.create_account(short_name="LaangUbot")
auth_url = r["auth_url"]

@Laang(["tg", "telegraph"], langs=True)
async def uptotelegraph(client: Client, message: Message, _):
    if not message.reply_to_message:
        return await message.reply(_['reply_media'])
    
    reply_message = message.reply_to_message
    if reply_message.media:
        m_d = await reply_message.download()
        try:
            media_url = upload_file(m_d)
            await message.reply(_['telegraph'].format(media_url[0]))
        except exceptions.TelegraphException as exc:
            await message.reply(_['err'].format(exc))
        finally:
            os.remove(m_d)
    elif reply_message.text:
        page_title = yins.get_text(message) or client.me.first_name
        page_text = reply_message.text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
            await message.reply(_['telegraph'].format(response['path']))
        except exceptions.TelegraphException as exc:
            await message.reply(_['err'].format(exc))

CMD_HELP.update(
    {
        "telegraph": (
            "telegraph",
            {
                "tg": "Balas ke Pesan Teks atau Media untuk mengunggahnya ke telegraph.",
            }
        )
    }
)
