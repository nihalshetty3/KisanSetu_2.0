from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.database import Base

class CropListing(Base):
    __tablename__="crop_listings"

    id=Column(Integer,primary_key=True,index=True)

    crop_name=Column(
        String(100),
        nullable=False
    )
    quantity = Column(
        Float,
        nullable=False
    )
    unit = Column(
        String(20),
        nullable=False
    )

    expected_price = Column(
        Float,
        nullable=False
    )  

    location = Column(
        String(150),
        nullable=False
    )

    status = Column(
        String(20),
        default="ACTIVE"
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
