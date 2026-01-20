import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

async def main():
    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Missing Telegram credentials")

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Hello! Your GitHub Actions bot is working."
    )

if __name__ == "__main__":
    asyncio.run(main())
