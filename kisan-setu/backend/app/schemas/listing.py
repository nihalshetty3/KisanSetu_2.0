from pydantic import BaseModel

class FarmerListing(BaseModel):
    crop_name: str
    quantity: float
    unit: str
    expected_price: float
    location: str
    
    