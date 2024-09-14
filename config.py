from os import getenv
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv(".env")

# Flood and old message dictionaries
flood = {}
OLD_MSG = {}

# Default message for spam prevention
MSG_PERMIT = """
╭━━━━━━━━━━━━━━━━━━━╮
┃ ✨ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴, 𝚃𝙾𝙳 ✨
╰━━━━━━━━━━━━━━━━━━━╯
⚠️ 𝙳𝙾𝙽'𝚃 𝚂𝙿𝙰𝙼 𝙼𝚈 𝙲𝙷𝙰𝚃, 𝙺𝙴𝙽𝚃𝙾𝙳
⚠️ 𝙸'𝙻𝙻 𝙰𝚄𝚃𝙾-𝙱𝙻𝙾𝙲𝙺 𝙸𝙵 𝚈𝙾𝚄 𝚂𝙿𝙰𝙼
⚠️ 𝚆𝙰𝙸𝚃 𝚄𝙽𝚃𝙸𝙻 𝙸 𝙰𝙲𝙲𝙴𝙿𝚃 𝚈𝙾𝚄𝚁 𝙼𝙴𝚂𝚂𝙰𝙶𝙴
╭━━━━━━━━━━━━━━━━━━━╮
┃ ✨ 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙸𝙲 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 ✨
┃ ✨ 𝙻𝚊𝚊𝚗𝚐 𝚄𝙱𝙾𝚃 ✨
╰━━━━━━━━━━━━━━━━━━━╯
"""

class Var:
    # Environment variables
    API_HASH = getenv("API_HASH")
    API_ID = getenv("API_ID")
    if API_ID:
        API_ID = int(API_ID)
    else:
        API_ID = None  # Berikan nilai default jika perlu
    ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/43d490b38cc1199e1706d.jpg")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Hey, Saya LaangUbot Dibuat dengan basis pyrogram versi terbaru")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283, -1001675396283]
    else:
        BLACKLIST_CHAT = [int(x) for x in BLACKLIST_CHAT.split(',')]
    LOG_CHAT = int(getenv("LOG_CHAT", 0))
    HNDLR = getenv("HNDLR", ".!*-^?").split()
    DB_URL = getenv("DATABASE_URL", "")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    MONGO_URI = getenv("MONGO_URI", None)
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split() if x]
    PMPERMIT = getenv("PMPERMIT", "True") == "True"
    PERMIT_MSG = getenv("PERMIT_MSG", MSG_PERMIT)
    PERMIT_LIMIT = int(getenv("PERMIT_LIMIT", 5))
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "WEnHwQnst3E2HzjGgwmy4UpB")
    STRING_1 = getenv("STRING_1", "")
    STRING_2 = getenv("STRING_2", "")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
    TZ = getenv("TZ", "Asia/Jakarta")
