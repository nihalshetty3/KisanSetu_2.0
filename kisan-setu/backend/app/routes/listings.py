from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.schemas.listing import FarmerListing
from app.database import get_db
from app.models.listing import CropListing


router = APIRouter(
    prefix="/api/voice",
    tags=["Voice"]
)

@router.post("/listing")
def create_voice_listing(listing: FarmerListing,db:Session=Depends(get_db)):

    new_listing=CropListing(
         crop_name=listing.crop_name,
         quantity=listing.quantity,
         unit=listing.unit,
         expected_price=listing.expected_price,
         location=listing.location
    )

    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    
    return {
        "success": True,
        "message": "Farmer listing received succesfully",
        "listing_id": new_listing.id
    }
    