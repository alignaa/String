import sys
from pyrogram import Client
from String.config import API_ID, API_HASH, BOT_TOKEN, LOGGER, LOG_GROUP

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_id=API_ID,
            api_hash=API_HASH,
            plugins={"root": "String/plugins"},
            bot_token=BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            is_bot = await self.get_me()
            self.username = is_bot.username
            self.namebot = is_bot.first_name
            self.LOGGER(__name__).info(
                f"BOT_TOKEN detected!\n"
                f"Username: @{self.username}\n"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(f"Error saat memulai bot: {e}")
            sys.exit()

        try:
            db_channel = await self.get_chat(LOG_GROUP)
            self.db_channel = db_channel
            await self.send_message(chat_id=db_channel.id, text="Bot Aktif!\n")
            self.LOGGER(__name__).info(
                "CHANNEL_DB Detected!\n"
                f"Title: {db_channel.title}\n"
                f"Chat ID: {db_channel.id}\n"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan @{self.username}\n "
                f"menjadi Admin di LOG_GROUP\n")
            sys.exit()

        self.LOGGER(__name__).info(
            "🔥 Bot Aktif! 🔥\n\n"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Berhenti!\n\n")