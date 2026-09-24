from fastapi import APIRouter , HTTPException
from pydantic import BaseModel

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
    
    valid_crop_ids=[1, 2, 3]
    if bid.crop_id not in valid_crop_ids:
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
    return {
        "success": True,
        "message": "Bid Placed succesfully",
        "bid": new_bid
    }