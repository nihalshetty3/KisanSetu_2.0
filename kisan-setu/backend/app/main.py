from fastapi import FastAPI

from app.database import Base, engine
from app.models.listing import CropListing
from app.models.farmer import Farmer
from app.models.bid import Bid



from app.routes.listings import router as listing_router
from app.routes.crops import router as crops_router
from app.routes.bids import router as bids_router 
from app.routes.sms import router as sms_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="KisanSetu API",
    description="Voice-first agricultural marketplace",
    version="1.0.0"
)

app.include_router(listing_router)
app.include_router(crops_router)
app.include_router(bids_router)
app.include_router(sms_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to KisanSetu"
    }