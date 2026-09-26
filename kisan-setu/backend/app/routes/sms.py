from fastapi import APIRouter
from pydantic import BaseModel

from app.routes.bids import bids
from app.routes.crops import crops


router = APIRouter(
    prefix="/api/sms",
    tags=["SMS"]
)


class SMSReply(BaseModel):
    phone: str
    message: str


@router.post("/reply")
def handle_sms_reply(sms: SMSReply):

    farmer_crop = None
    pending_bid = None

    # Find the pending bid belonging to this farmer
    for bid in bids:

        crop = next(
            (
                crop
                for crop in crops
                if crop["id"] == bid["crop_id"]
            ),
            None
        )

        if (
            crop
            and crop["farmer_phone"] == sms.phone
            and bid["status"] == "pending"
        ):
            farmer_crop = crop
            pending_bid = bid
            break

    # No pending bid found
    if pending_bid is None:
        return {
            "success": False,
            "message": "No pending bid found for this farmer"
        }

    # Clean SMS response
    response = sms.message.strip()

    # 1 = Accept
    if response == "1":

        pending_bid["status"] = "accepted"

        return {
            "success": True,
            "message": "Bid accepted successfully",
            "bid": pending_bid
        }

    # 2 = Reject
    elif response == "2":

        pending_bid["status"] = "rejected"

        return {
            "success": True,
            "message": "Bid rejected successfully",
            "bid": pending_bid
        }

    # 3 = Waiting
    elif response == "3":

        pending_bid["status"] = "waiting"

        return {
            "success": True,
            "message": "Bid marked as waiting",
            "bid": pending_bid
        }

    # Invalid SMS
    else:

        return {
            "success": False,
            "message": "Invalid response. Reply 1 to accept, 2 to reject, or 3 to wait."
        }