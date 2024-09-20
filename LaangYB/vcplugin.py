from fipper.types import Message
from pyLaang import Laang, CMD_HELP
from pyLaang.Clients.pytgcalls import VcMusic
from . import yins

@Laang(["play"], langs=True)
async def play(client, msg: Message, _):
    Vc = VcMusic(client, msg)
    me = await client.get_me()
    replied = msg.reply_to_message
    chat_id = msg.chat.id
    if replied:
        if replied.audio or replied.voice:
            await msg.delete()
            huehue = await msg.reply(_["play_1"])
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                duration = replied.audio.duration
                songname = replied.audio.title[:35] + "..." if replied.audio.title else replied.audio.file_name[:35] + "..."
            elif replied.voice:
                duration = replied.voice.duration
                songname = "Voice Note"
            if chat_id in yins.queue:
                pos = yins.add_to_queue(chat_id, songname, dl, link, "Audio", 128)
                await huehue.delete()
                await msg.reply_photo(
                    photo="https://telegra.ph/file/d6f92c979ad96b2031cba.png",
                    caption=_["play_3"].format(pos=pos, url=link, song=songname, duration_min=duration, chat_ids=chat_id, from_users=me.mention)
                )
            else:
                if not (await Vc.JoinVc()):
                    await Vc.JoinVc()
                await client.group_call.start_audio(dl)
                yins.add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.delete()
                await msg.reply_photo(
                    photo="https://telegra.ph/file/6213d2673486beca02967.png",
                    caption=_["play_2"].format(url=link, song=songname, duration_min=duration, chat_ids=chat_id, from_users=me.mention)
                )
            os.remove(dl)
            return
    if len(msg.command) < 2:
        await msg.reply(_["play_4"])
    else:
        query = yins.get_cmd(msg)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = yins.yt_info_query(query)
        if title == 0:
            return await msg.reply_text(_["play_5"])
        else:
            xx = await msg.reply_text(_["play_1"])
            url = f"https://www.youtube.com/watch?v={videoid}"
            title, duration_min, duration_sec, thumbnail = yins.yt_info_id(videoid)
            file_path, direct = await yins.download(videoid, videoid=True)
            thumbs = await yins.gen_thumb(
                client=client,
                videoid=videoid,
                file_path=file_path,
                cache=cache.format(videoid),
                cache_thumb=cache_thumb.format(videoid),
                fonts=font,
                fonts2=font2,
            )
            if chat_id in yins.queue:
                pos = yins.add_to_queue(chat_id, title, file_path, url, "Audio", 128)
                await msg.reply_photo(
                    photo=thumbs,
                    caption=_["play_3"].format(pos=pos, url=url, title=title, duration_min=duration_min, chat_ids=chat_id, from_users=me.mention),
                )
            else:
                if not (await Vc.JoinVc()):
                    await Vc.JoinVc()
                await client.group_call.start_audio(file_path)
                yins.add_to_queue(chat_id, title, file_path, url, "Audio", 128)
                await msg.reply_photo(
                    photo=thumbs,
                    caption=_["play_2"].format(url=url, title=title, duration_min=duration_min, chat_ids=chat_id, from_users=me.mention),
                )
            await xx.delete()

@Laang(["end"], langs=True)
async def end_play(client, m: Message, _):
    chat_id = m.chat.id
    if chat_id in yins.queue:
        try:
            await client.group_call.leave()
            yins.clear_queue(chat_id)
            await m.edit(_["play_6"])
        except Exception as e:
            await m.reply(str(e))
    else:
        await m.edit(_["play_7"])

@Laang(["skip"], langs=True)
async def skip(client, m: Message, _):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await yins.skip_song(client, chat_id)
        if op == 0:
            await m.reply(_["play_8"])
        elif op == 1:
            await m.reply(_["play_9"])
        else:
            await m.reply(
                _["play_10"].format(op[1], op[0], op[2]),
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = _["play_11"]
        if chat_id in yins.queue:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x != 0:
                    hm = await yins.skip_item(chat_id, x)
                    if hm != 0:
                        OP += f"\n<b>#⃣{x}</b> - {hm}"
            await m.reply(OP)

@Laang(["playlist"], langs=True)
async def playlist(client, m: Message, _):
    try:
        chat_id = m.chat.id
        if chat_id in yins.queue:
            chat_queue = yins.get_queue(chat_id)
            if len(chat_queue) == 1:
                await m.reply(
                    _["play_12"].format(chat_queue[0][2], chat_queue[0][0], chat_queue[0][3]),
                    disable_web_page_preview=True,
                )
            else:
                QUE = _["play_13"].format(chat_queue[0][2], chat_queue[0][0], chat_queue[0][3])
                l = len(chat_queue)
                for x in range(1, l):
                    hmm = chat_queue[x][0]
                    hmmm = chat_queue[x][2]
                    hmmmm = chat_queue[x][3]
                    QUE += f"\n#{x} - [{hmm}]({hmmm}) | {hmmmm}\n"
                await m.reply(QUE, disable_web_page_preview=True)
        else:
            await m.reply(_["play_7"])
    except Exception as e:
        await m.reply(str(e))

@Laang(["pause"], langs=True)
async def pause(client, m: Message, _):
    if m.chat.id in yins.queue:
        await client.group_call.set_pause(True)
        await m.reply_text(_["play_14"])
    else:
        await m.reply(_["play_7"])

@Laang(["resume"], langs=True)
async def resume(client: Client, m: Message, _):
    if m.chat.id in yins.queue:
        await client.group_call.set_pause(False)
        await m.reply_text(_["play_15"])
    else:
        await m.reply(_["play_7"])

CMD_HELP.update(
    {"vcplugin": (
        "vcplugin",
        {
            "play [text/reply/url]": "Untuk Memutar musik",
            "vplay [text/reply/url]": "Untuk memutar video",
            "end": "Untuk menghentikan musik yang diputar",
            "playlist": "Melihat daftar list musik selanjutnya.",
            "pause": "Jeda streaming yang sedang dimainkan.",
            "resume": "Lanjutkan streaming yang di jeda.",
            "skip": "Melewati musik/video yang diputar",
        }
    )}
)
