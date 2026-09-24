from fastapi import APIRouter
from app.schemas.listing import FarmerListing

router = APIRouter(
    prefix="/api/voice",
    tags=["Voice"]
)

@router.post("/listing")
def create_voice_listing(listing: FarmerListing):
    print("\n==== Farmer Listing====")
    
    print(f"Crop: {listing.crop_name}")
    print(f"Quantity {listing.quantity} {listing.unit}")
    print(f"Expected Price: {listing.expected_price}")
    print(f"Location: {listing.location}")
    print("==========================")
    
    return {
        "success": True,
        "message": "Farmer listing received succesfully"
    }
    