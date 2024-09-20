import os
import re
import aiofiles
from fipper import Client
from fipper.types import Message
from pyLaang import Laang, CMD_HELP, tgbot
from pyLaang.pyrogram import eor

from . import yins

@Laang(["paste", "pst"], langs=True)
async def paste_func(client: Client, message: Message, _):
    if not message.reply_to_message:
        return await eor(message, _['reply'])

    r = message.reply_to_message
    if not r.text and not r.document:
        return await eor(message, _['paste_1'])

    m = await eor(message, _['p'])
    
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit(_['paste_2'])
        
        pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")
        if not pattern.search(r.document.mime_type):
            return await m.edit(_['paste_3'])
        
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    
    done, key = await yins.get_paste(content)
    if not done:
        return await m.edit(key)
    
    link = f"https://spaceb.in/{key}"
    raw = f"https://spaceb.in/api/v1/documents/{key}/raw"
    
    try:
        if tgbot:
            try:
                tgbot.me = await tgbot.get_me()
                results = await client.get_inline_bot_results(tgbot.me.username, f"paste-{key}")
                await message.reply_inline_bot_result(
                    results.query_id,
                    results.results[0].id,
                    reply_to_message_id=yins.ReplyCheck(message),
                )
            except Exception as e:
                await m.edit(str(e))
        else:
            await message.reply_photo(
                photo=link,
                quote=False,
                caption=_['paste_4'].format(link, raw),
            )
        await m.delete()
    except Exception as e:
        await m.edit(_['err'].format(e))

CMD_HELP.update(
    {"paste": (
        "paste",
        {
            "paste": "Menyimpan teks ke layanan pastebin.",
        }
    )}
)
