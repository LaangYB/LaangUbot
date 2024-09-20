# Laang - Ubot
# Copyright (C) 2024 @LaangYB
#
# This file is a part of < https://github.com/LaangYB/LaangUbot >
# Please read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUbot/blob/main/LICENSE/>.
#
# FROM LaangUbot <https://github.com/LaangYB/LaangUbot>
# t.me/ybtraviss & t.me/ybtravisss

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from git import Repo

from pyLnnggg import Laang, CMD_HELP, tgbot
from . import yins

@Laang(["update"], langs=True)
async def updater(client, msg, _):
    xx = await eor(msg, _['p'])
    m = await yins.updater()
    repo = Repo.init()
    branch = repo.active_branch
    changelog, tl_chnglog = await yins.gen_chlog(
        repo, f"HEAD..upstream/{branch}"
    )
    if m:
        try:
            tgbot.me = await tgbot.get_me()
            results = await client.get_inline_bot_results(tgbot.me.username, f"in_update")
            await msg.reply_inline_bot_result(
                results.query_id,
                results.results[0].id,
                reply_to_message_id=yins.ReplyCheck(msg),
            )
            await xx.delete()
        except Exception as e:
            return await eor(msg, _['err'].format(e))
    else:
        await xx.edit(
            _['update'].format(branch, branch),
            disable_web_page_preview=True,
        )

CMD_HELP.update(
    {"update": (
        "update",
        {
            "update": "Pake Ini Untuk Mengecek Userbot lu Versi Terbaru."
        }
    )}
)
