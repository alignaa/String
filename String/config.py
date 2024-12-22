from os import getenv
from dotenv import load_dotenv
from logging import basicConfig, INFO, WARNING, getLogger, Logger

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
LOG_GROUP = int(getenv("LOG_GROUP", ""))

basicConfig(level=INFO, format="[%(levelname)s] - %(message)s")
getLogger("pyrogram").setLevel(WARNING)
def LOGGER(name: str) -> Logger:
    return getLogger(name)