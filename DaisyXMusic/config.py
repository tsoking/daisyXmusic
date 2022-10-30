from os import getenv

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/DESTROYED_HOME")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/0950961829571c518df94.jpg")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
PROJECT_NAME = getenv("PROJECT_NAME", "")
SOURCE_CODE = getenv("SOURCE_CODE", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
