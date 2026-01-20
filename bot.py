import os
import asyncio
import snscrape.modules.twitter as sntwitter
from telegram import Bot

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

TWITTER_USERNAME = "elonmusk"   # 👈 change later if needed

async def main():
    # --- sanity check ---
    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Missing Telegram credentials")

    print(f"Fetching latest tweet from @{TWITTER_USERNAME}")

    # --- fetch latest tweet ---
    scraper = sntwitter.TwitterUserScraper(TWITTER_USERNAME)
    tweet = next(scraper.get_items(), None)

    if tweet is None:
        print("No tweets found")
        return

    # --- extract data ---
    tweet_id = tweet.id
    tweet_text = tweet.content
    tweet_url = tweet.url
    media_urls = []

    if tweet.media:
        for media in tweet.media:
            if hasattr(media, "fullUrl"):
                media_urls.append(media.fullUrl)

    # --- print output (for now) ---
    print("TWEET ID:", tweet_id)
    print("TWEET URL:", tweet_url)
    print("TEXT:")
    print(tweet_text)

    if media_urls:
        print("MEDIA:")
        for m in media_urls:
            print(m)
    else:
        print("NO MEDIA")

    print("DONE")

if __name__ == "__main__":
    asyncio.run(main())
