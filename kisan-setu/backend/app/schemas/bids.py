from pydantic import BaseModel

class BidCreate(BaseModel):
    crop_id:int
    buyer_id:int
    bid_price:float
    quantity:float 

    