from sqlalchemy import Column,Integer,Float,String,ForeignKey

from app.database import Base

class Bid(Base):
     __tablename__="bids"

     bid_id = Column(
        Integer,
        primary_key=True,
        index=True
     )

     crop_id = Column(
        Integer,
        ForeignKey("crops.crop_id"),
        nullable=False
    )

     buyer_id = Column(
        Integer,
        nullable=False
     )

     bid_price = Column(
        Float,
        nullable=False
     )

     quantity = Column(
        Float,
        nullable=False
     )

     status = Column(
        String(20),
        default="PENDING"
     )

     

