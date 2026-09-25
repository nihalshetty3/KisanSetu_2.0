from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.crop import Crop


router = APIRouter(
    prefix="/api/crops",
    tags=["Crops"]
)


@router.get("/")
def get_all_crops(db:Session=Depends(get_db)):

    listings=db.query(Crop).all()


    return {
        "success": True,
        "count": len(listings),
        "listings": [
            {
                "listing_id": listing.crop_id,
                "farmer_id": listing.farmer_id,
                "crop_name": listing.crop_name,
                "quantity": listing.quantity,
                "unit": listing.unit,
                "expected_price": listing.expected_price,
                "location": listing.location
            }
            for listing in listings
        ]
    }

