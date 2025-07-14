import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto

# Load secrets
load_dotenv()
api_id     = os.getenv("tg_api_id")
api_hash   = os.getenv("tg_api_hash")
session_name = os.getenv("session_name")

# Logging setup
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ensure_directory(path):
    os.makedirs(path, exist_ok=True)

def scrape_channel_messages(channel_username, limit=100):
    with TelegramClient(session_name, api_id, api_hash) as client:
        messages_data = []
        today = datetime.now().strftime('%Y-%m-%d')
        raw = f"Data/Raw/Telegram_Med_messages/{today}"
        ensure_directory(raw)
        file_path = os.path.join(raw, f"{channel_username.replace('@', '')}.json")

        try:
            for message in client.iter_messages(channel_username, limit=limit):
                if message.text or message.media:
                    msg = {
                        'message_id': message.id,
                        'date': str(message.date),
                        'sender_id': message.sender_id,
                        'text': message.text,
                        'media_type': type(message.media).__name__ if message.media else None
                    }
                    messages_data.append(msg)

                    # Save image files if media exists
                    if isinstance(message.media, MessageMediaPhoto):
                        img_dir = os.path.join(raw, "images")
                        ensure_directory(img_dir)
                        img_path = os.path.join(img_dir, f"{channel_username.replace('@', '')}_{message.id}.jpg")
                        client.download_media(message, img_path)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(messages_data, f, indent=2, ensure_ascii=False)

            logging.info(f"Successfully scraped {len(messages_data)} messages from {channel_username}")

        except Exception as e:
            logging.error(f"Error scraping {channel_username}: {e}")