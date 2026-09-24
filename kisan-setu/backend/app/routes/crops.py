from fastapi import APIRouter

router = APIRouter(
    prefix="/api/crops",
    tags=["Crops"]
)

crops = [
    {
        "id": 1,
        "farmer_id": 101,
        "farmer_phone": "+919999999999",
        "crop_name": "tomato",
        "quantity": 500,
        "unit": "kg",
        "expected_price": 25,
        "location": "Mangalore"
    },
    {
        "id": 2,
        "farmer_id": 102,
        "farmer_phone": "+918888888888",
        "crop_name": "rice",
        "quantity": 1000,
        "unit": "kg",
        "expected_price": 42,
        "location": "Udupi"
    },
    {
        "id": 3,
        "farmer_id": 103,
        "farmer_phone": "+917777777777",
        "crop_name": "onion",
        "quantity": 300,
        "unit": "kg",
        "expected_price": 30,
        "location": "Mangalore"
    }
]


@router.get("/")
def get_all_crops():
    return {
        "success": True,
        "count": len(crops),
        "crops": crops
    }