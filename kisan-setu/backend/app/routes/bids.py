from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.bid import Bid
from app.models.crop import Crop
from app.schemas.bids import BidCreate

router=APIRouter(
      prefix="/api/bids",
      tags=["Bids"]
)

@router.post("/")
def create_bid(
     bid: BidCreate,
    db: Session = Depends(get_db)
):

    crop=db.query(Crop).filter(
           Crop.crop_id==bid.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop listing not found"
        )

    new_bid = Bid(
        crop_id=bid.crop_id,
        buyer_id=bid.buyer_id,
        bid_price=bid.bid_price,
        quantity=bid.quantity
    )

    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)

    return {
        "success": True,
        "message": "Bid created successfully",
        "bid_id": new_bid.bid_id
    }

@router.get("/")
def get_all_bids(
    db: Session = Depends(get_db)
):

    bids=db.query(Bid).all()

    return {
        "success": True,
        "count": len(bids),
        "bids": [
            {
                "bid_id": bid.bid_id,
                "crop_id": bid.crop_id,
                "buyer_id": bid.buyer_id,
                "bid_price": bid.bid_price,
                "quantity": bid.quantity,
                "status": bid.status
            }
            for bid in bids
        ]
    }

@router.get("/{bid_id}")
def get_bid(
    bid_id: int,
    db: Session = Depends(get_db)
):
    bid = db.query(Bid).filter(
        Bid.bid_id == bid_id
    ).first()

    if not bid:
        raise HTTPException(
            status_code=404,
            detail="Bid not found"
        )

    return {
        "success": True,
        "bid": {
            "bid_id": bid.bid_id,
            "crop_id": bid.crop_id,
            "buyer_id": bid.buyer_id,
            "bid_price": bid.bid_price,
            "quantity": bid.quantity,
            "status": bid.status
        }
    }

@router.get("/listing/{crop_id}")
def get_bids_for_listing(
    crop_id: int,
    db: Session = Depends(get_db)
):
     
    bids = db.query(Bid).filter(
        Bid.crop_id == crop_id
    ).all()
     

    return {
        "success": True,
        "crop_id": crop_id,
        "count": len(bids),
        "bids": [
            {
                "bid_id": bid.bid_id,
                "buyer_id": bid.buyer_id,
                "bid_price": bid.bid_price,
                "quantity": bid.quantity,
                "status": bid.status
            }
            for bid in bids
        ]
    }

