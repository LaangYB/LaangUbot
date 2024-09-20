from fipper.types import Message

from pyLnnggg import CMD_HELP
from pyLnnggg.dB.variable import del_var, get_var, set_var
from pyLnnggg.decorator import Laang
from . import yins

@Laang(["set_var"], langs=True)
async def setdv_handler(client, m: Message, _):
    cmd = m.command[1] if len(m.command) > 1 else None
    value = m.text.split(None, 2)[2] if len(m.text.split(None, 2)) > 2 else None
    if not cmd or not value:
        return await m.reply(_["vars_1"])
    else:
        await set_var(cmd, value)
        return await m.reply(_["vars_2"].format(cmd, value))

@Laang(["del_var"], langs=True)
async def deldv_handler(client, m: Message, _):
    cmd = yins.get_cmd(m)
    if not cmd:
        return await m.reply(_["vars_3"])
    else:
        await del_var(cmd)
        return await m.reply(_["vars_4"].format(cmd))

@Laang(["get_var"], langs=True)
async def getdv_handler(client, m: Message, _):
    cmd = yins.get_cmd(m)
    if not cmd:
        return await m.reply(_["vars_5"])
    else:
        done = await get_var(cmd)
        if done:
            return await m.reply(_["vars_6"].format(cmd, done))
        else:
            return await m.reply(_["vars_7"])

CMD_HELP.update(
    {"vars": (
        "vars",
        {
            "set_var [variable, value]": "Set vars database.",
            "del_var [variable]": "Untuk menghapus vars database.",
            "get_var [variable]": "Untuk mendapatkan vars database.",
        }
    )}
)
