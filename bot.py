import os
import asyncio
import requests
import feedparser
from telegram import Bot

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

TWITTER_USERNAME = "elonmusk"

NITTER_INSTANCES = [
    "https://nitter.net",
    "https://nitter.it",
    "https://nitter.privacydev.net",
    "https://nitter.poast.org",
]

async def fetch_latest_tweet():
    for base in NITTER_INSTANCES:
        url = f"{base}/{TWITTER_USERNAME}/rss"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code != 200:
                continue

            feed = feedparser.parse(r.text)
            if not feed.entries:
                continue

            return feed.entries[0]

        except Exception:
            continue

    return None

async def main():
    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Missing Telegram credentials")

    print(f"Fetching latest tweet from @{TWITTER_USERNAME}")

    entry = await fetch_latest_tweet()

    if not entry:
        print("Could not fetch tweet from any Nitter instance")
        return

    title = entry.title
    link = entry.link

    print("TITLE:", title)
    print("LINK:", link)

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=f"🧵 New tweet from @{TWITTER_USERNAME}\n\n{title}\n\n{link}"
    )

if __name__ == "__main__":
    asyncio.run(main())
