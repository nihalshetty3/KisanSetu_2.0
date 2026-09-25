from sqlalchemy import Column ,Integer,String

from app.database import Base

class Farmer(Base):
     __tablename__ = "farmers"

     farmer_id = Column(
        Integer,
        primary_key=True,
        index=True
     )

     phone = Column(
        String(20),
        unique=True,
        nullable=False
     ) 