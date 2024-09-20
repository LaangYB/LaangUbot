from random import choice
from pyLaang import Laang, CMD_HELP
from pyLaang.Clients.client import tgbot

from . import yins, hndlr

@Laang(["openai", "ai", "ask"], langs=True)
async def open_ai(client: Client, message: Message, xd: dict):
    if len(message.command) == 1:
        await message.reply(f"Ketik <code>{choice(hndlr)}ai [question]</code> untuk menggunakan OpenAI")
        return
    
    question = yins.get_cmd(message)
    msg = await message.reply(xd["p"])
    
    try:
        ai_answer = await yins.ask_ai(question)
        await msg.edit(ai_answer)
    except Exception as e:
        await msg.edit(xd["err"].format(e))

CMD_HELP.update(
    {"openai": (
        "openai",
        {
            "ai": "Tanyakan pertanyaan anda dan AI akan menjawabnya.",
        }
    )}
)
