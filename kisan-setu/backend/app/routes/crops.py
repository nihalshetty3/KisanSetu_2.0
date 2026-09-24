from fastapi import APIRouter 
router = APIRouter(
    prefix="/api/crops",
    tags=["Crops"]
)

crops=[
{
        "id": 1,
        "crop_name": "tomato",
        "quantity": 500,
        "unit": "kg",
        "expected_price": 25,
        "location": "Mangalore"
    },
    {
        "id": 2,
        "crop_name": "rice",
        "quantity": 1000,
        "unit": "kg",
        "expected_price": 42,
        "location": "Udupi"
    },
    {
        "id": 3,
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