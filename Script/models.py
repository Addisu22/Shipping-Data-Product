from sqlalchemy import Column, Integer, String, DateTime
from dbconnection import Base

# Adjust according to our actual dbt models
class ProductMention(Base):
    __tablename__ = "product_mentions"  # Our dbt model table name
    
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    mention_count = Column(Integer)
    channel = Column(String)
    timestamp = Column(DateTime)

class ChannelActivity(Base):
    __tablename__ = "channel_activity"  # Our dbt model table name
    
    id = Column(Integer, primary_key=True, index=True)
    channel_name = Column(String)
    post_count = Column(Integer)
    date = Column(DateTime)

class Message(Base):
    __tablename__ = "messages"  # Our dbt model table name
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    channel = Column(String)
    timestamp = Column(DateTime)