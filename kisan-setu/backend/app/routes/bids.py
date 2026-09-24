from fastapi import APIRouter , HTTPException
from pydantic import BaseModel

from app.routes.crops import crops
from app.services.notification_service import send_farmer_notification

router = APIRouter(
    prefix="/api/bids",
    tags=["Bids"]
)

bids=[]

class BidCreate(BaseModel):
    crop_id: int
    buyer_id: int
    bid_price: int
    
@router.post("/")
def create_bid(bid: BidCreate):
    
    crop = next(
        (crop for crop in crops if crop["id"] == bid.crop_id),
        None
    )
    
    if crop is None:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )
        
    new_bid = {
        "id": len(bids) + 1,
        "crop_id": bid.crop_id,
        "buyer_id": bid.buyer_id,
        "bid_price": bid.bid_price,
        "status": "pending"
    }
    
    bids.append(new_bid)
    
    notification = send_farmer_notification(
        farmer_phone=crop["farmer_phone"],
        crop_name=crop["crop_name"],
        bid_price=bid.bid_price,
        quantity=crop["quantity"],
        unit=crop["unit"]
    )
    return {
        "success": True,
        "message": "Bid Placed succesfully",
        "bid": new_bid,
        "notification": notification
    }