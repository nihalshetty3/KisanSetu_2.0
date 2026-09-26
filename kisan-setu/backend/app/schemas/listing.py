from pydantic import BaseModel

class ListingCreate(BaseModel):
    farmer_id:int
    crop_name:str
    quantity: float
    unit: str
    expected_price:float
    location:str
    
    
    