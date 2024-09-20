from time import sleep
from contextlib import suppress
from pyLaang import Laang, CMD_HELP, Yins
from pyLaang.types import Client, Message
from . import yins

@Laang(['startvc'], group_only=True, langs=True)
async def start_vcs(client: Client, msg: Message, _):
    yb = await eor(msg, _["vctol_1"])
    title = yins.get_cmd(msg)
    try:
        if title:
            await Yins.StartVc(client, msg, title)
            await yb.edit(_["vctol_2"].format(title, msg.chat.title, msg.chat.id))
        else:
            await Yins.StartVc(client, msg)
            await yb.edit(_["vctol_3"].format(msg.chat.title, msg.chat.id))
    except Exception as e:
        await msg.reply(str(e))

@Laang(["stopvc"], group_only=True, langs=True)
async def end_vc_(client: Client, message: Message, _):
    """End group call"""
    chat_id = message.chat.id
    await Yins.StopVc(client, message)
    await eor(message, _["vctol_4"].format(chat_id))

@Laang(["joinvcs", "jovcs"], group_only=True, devs=True)
@Laang(["joinvc"], group_only=True, langs=True)
async def joinvc(client: Client, message: Message, _):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    xx = await message.reply(_["p"])
    try:
        chat_id = int(chat_id)
        await client.group_call.start(chat_id)
        await xx.edit(_["vctol_5"].format(client.me.mention, chat_id))
        sleep(5)
        try:
            await client.group_call.set_is_mute(True)
        except Exception:
            sleep(5)
            await client.group_call.set_is_mute(True)
    except Exception as e:
        await xx.edit(_["err"].format(str(e)))

@Laang(["leavevcs", "levcs"], group_only=True, devs=True)
@Laang(["leavevc", "lvc"], group_only=True, langs=True)
async def leavevc(client: Client, message: Message, _):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    xx = await message.reply(_["p"])
    try:
        chat_id = int(chat_id)
        await client.group_call.stop()
        await xx.edit(_['vctol_6'].format(client.me.mention, chat_id))
    except Exception as e:
        await message.reply(_["err"].format(str(e)))

CMD_HELP.update(
    {"vctools": (
        "vctools",
        {
            "startvc": "Memulai Obrolan Suara Di Grup",
            "stopvc": "Mengakhiri Obrolan Suara Di Grup",
            "joinvc": "Bergabung Ke Obrolan Suara Di Grup",
            "leavevc": "Meninggalkan Obrolan Suara Di Grup",
        }
    )}
)
