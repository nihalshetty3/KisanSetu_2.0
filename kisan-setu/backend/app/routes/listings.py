from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.schemas.listing import ListingCreate
from app.database import get_db
from app.models.listing import CropListing
from app.models.crop import Crop



router = APIRouter(
    prefix="/api/voice",
    tags=["Voice"]
)

@router.post("/listing")
def create_voice_listing(listing: ListingCreate,db:Session=Depends(get_db)):

    new_listing=Crop(
        farmer_id=listing.farmer_id,
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
        "listing_id": new_listing.crop_id
    }
    