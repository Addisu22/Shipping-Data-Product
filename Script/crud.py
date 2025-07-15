from sqlalchemy.orm import Session
from models import ProductMention, ChannelActivity, Message
from typing import List, Optional

def get_top_products(db: Session, limit: int = 10) -> List[ProductMention]:
    return db.query(ProductMention)\
             .order_by(ProductMention.mention_count.desc())\
             .limit(limit)\
             .all()

def get_channel_activity(db: Session, channel_name: str) -> List[ChannelActivity]:
    return db.query(ChannelActivity)\
             .filter(ChannelActivity.channel_name == channel_name)\
             .order_by(ChannelActivity.date)\
             .all()

def search_messages(db: Session, query: str) -> List[Message]:
    return db.query(Message)\
             .filter(Message.content.ilike(f"%{query}%"))\
             .order_by(Message.timestamp.desc())\
             .all()