from fastapi import FastAPI, Depends, HTTPException
from typing import List
from database import get_db
from sqlalchemy.orm import Session
import Script.cruds as cruds
import schemas

app = FastAPI(
    title="Social Media Analytics API",
    description="API for analyzing social media data processed by dbt",
    version="0.1.0"
)

@app.get("/api/reports/top-products", response_model=List[schemas.ProductMentionResponse])
def get_top_products(limit: int = 10, db: Session = Depends(get_db)):
    """
    Returns the most frequently mentioned products.
    
    - **limit**: Number of top products to return (default: 10)
    """
    products = cruds.get_top_products(db, limit=limit)
    if not products:
        raise HTTPException(status_code=404, detail="No product mentions found")
    return products

@app.get("/api/channels/{channel_name}/activity", response_model=List[schemas.ChannelActivityResponse])
def get_channel_activity(channel_name: str, db: Session = Depends(get_db)):
    """
    Returns the posting activity for a specific channel.
    
    - **channel_name**: Name of the channel to get activity for
    """
    activity = cruds.get_channel_activity(db, channel_name=channel_name)
    if not activity:
        raise HTTPException(
            status_code=404, 
            detail=f"No activity found for channel {channel_name}"
        )
    return activity

@app.get("/api/search/messages", response_model=List[schemas.MessageResponse])
def search_messages(query: str, db: Session = Depends(get_db)):
    """
    Searches for messages containing a specific keyword.
    
    - **query**: Keyword to search for in messages
    """
    messages = cruds.search_messages(db, query=query)
    if not messages:
        raise HTTPException(
            status_code=404, 
            detail=f"No messages found containing '{query}'"
        )
    return messages