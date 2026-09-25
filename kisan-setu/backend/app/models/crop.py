from sqlalchemy import Column ,Integer,String,Float,ForeignKey

from app.database import Base

class Crop(Base):
    __tablename__="crops"

    crop_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    farmer_id = Column(
        Integer,
        ForeignKey("farmers.farmer_id"),
        nullable=False
    )

    crop_name = Column(
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