import os

from fipper import Client
from fipper.types import Message

from pyLaang import Laang, CMD_HELP
from pyLaang.pyrogram import eor

from . import *

arguments = [
    "smallcap",
    "monospace",
    "outline",
    "script",
    "blackbubbles",
    "bubbles",
    "bold",
    "bolditalic"
]

fonts = arguments

_default = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_smallcap = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘϙʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ"
_monospace = "𝚊𝚋𝚌𝚍𝚎𝚋𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚟𝚠𝚝𝚋𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
_outline = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
_script = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒿𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
_blackbubbles = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
_bubbles = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
_bold = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
_bolditalic = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"

def gen_font(text, new_font):
    new_font = " ".join(new_font).split()
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text

@Laang(["font"])
async def font_yins(client: Client, message: Message):
    if message.reply_to_message or yins.get_cmd(message):
        font = yins.get_cmd(message)
        text = message.reply_to_message.text
        if not font:
            return await eor(message, f"<code>{font} Tidak Ada Dalam Daftar Font Kentod...</code>")
        
        font_map = {
            "smallcap": _smallcap,
            "monospace": _monospace,
            "outline": _outline,
            "script": _script,
            "blackbubbles": _blackbubbles,
            "bubbles": _bubbles,
            "bold": _bold,
            "bolditalic": _bolditalic
        }
        
        yinsYB = gen_font(text, font_map.get(font, _default))
        await eor(message, yinsYB)
    else:
        return await message.reply("Balas Teks Dan Isi Nama Font Yang Bener Bego!!!")

@Laang(["lf", "listfont"])
async def fonts(client: Client, msg: Message):
    await eor(
        msg,
        "<b>❯❯ Daftar Font ❮❮</b>\n"
        "<b>         ☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎</b>\n\n"
        "<b>• SmallCap » Laang</b>\n"
        "<b>• Monospace » Laang</b>\n"
        "<b>• Outline » Laang</b>\n"
        "<b>• Script » Laang</b>\n"
        "<b>• BlackBubbles » Laang</b>\n"
        "<b>• Bubbles » Laang</b>\n"
        "<b>• Bold » Laang</b>\n"
        "<b>• BoldItalic » Laang</b>\n\n"
        "<b>   ✧ Laang Ubot ✧</b>"
    )

CMD_HELP.update(
    {"fonts": (
        "fonts",
        {
            "font <reply text>": "Membuat Text Dengan Gaya Font Berbeda.",
            "lf": "Untuk Melihat Daftar Font.",
        }
    )}
)
