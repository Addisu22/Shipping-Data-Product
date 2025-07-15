from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class ProductMentionResponse(BaseModel):
    product_name: str
    mention_count: int
    
    class Config:
        orm_mode = True

class ChannelActivityResponse(BaseModel):
    channel_name: str
    post_count: int
    date: datetime
    
    class Config:
        orm_mode = True

class MessageResponse(BaseModel):
    content: str
    channel: str
    timestamp: datetime
    
    class Config:
        orm_mode = True