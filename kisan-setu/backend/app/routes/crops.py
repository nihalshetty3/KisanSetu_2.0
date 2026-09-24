from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.listing import CropListing


router = APIRouter(
    prefix="/api/crops",
    tags=["Crops"]
)


@router.get("/")
def get_all_crops(db:Session=Depends(get_db)):
    crop=db.query(CropListing).all()

    return {
        "success": True,
        "count": len(crop),
        "crops": [
            {
                "id": crop.id,
                "crop_name": crop.crop_name,
                "quantity": crop.quantity,
                "unit": crop.unit,
                "expected_price": crop.expected_price,
                "location": crop.location,
                "status": crop.status,
                "created_at": crop.created_at
            }
            for crop in crop
        ]
    }

