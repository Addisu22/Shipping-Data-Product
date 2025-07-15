import os
import json
import logging
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_id     = os.getenv("tg_api_id")
api_hash   = os.getenv("tg_api_hash")
session_name = os.getenv("session_name")

# Setup logging
logging.basicConfig(
    filename="Telegram_Data_Scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ensure directories exist
def ensure_directory(path):
    os.makedirs(path, exist_ok=True)

# Scraper Function
async def scrape_channel(channel_username, limit=100):
    today = datetime.now().strftime('%Y-%m-%d')
    raw_base = f"Data/Raw/Telegram_messages/{today}"
    ensure_directory(raw_base)

    json_path = os.path.join(raw_base, f"{channel_username.replace('@', '')}.json")
    image_dir = os.path.join(raw_base, "images")
    ensure_directory(image_dir)

    messages_data = []

    async with TelegramClient(session_name, api_id, api_hash) as client:
        try:
            async for message in client.iter_messages(channel_username, limit=limit):
                if message.text or message.media:
                    msg = {
                        "id": message.id,
                        "sender_id": message.sender_id,
                        "date": str(message.date),
                        "text": message.text,
                        "channel": channel_username,
                        "media_type": type(message.media).__name__ if message.media else None
                    }
                    messages_data.append(msg)

                    # Download image if exists
                    if isinstance(message.media, MessageMediaPhoto):
                        img_path = os.path.join(image_dir, f"{channel_username.strip('@')}_{message.id}.jpg")
                        await client.download_media(message, img_path)

            # Save to JSON
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(messages_data, f, indent=2, ensure_ascii=False)
                
            # Setup Logging at the Top of our Script
            print(f"Scraped {len(messages_data)} messages from {channel_username}")
            logging.info(f"Scraped {len(messages_data)} messages from {channel_username}")

        except Exception as e:
            print(f"Error scraping {channel_username}: {e}")
            logging.error(f"Error scraping {channel_username}: {e}")
