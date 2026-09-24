def send_farmer_notification(
    farmer_phone: str,
    crop_name: str,
    bid_price: float,
    quantity: float,
    unit: str
):
    
    message = (
        f"KisanSetu: You received a new bid of"
        f"₹{bid_price}/{unit} for your {quantity}{unit}"
        f"of {crop_name}"
    )
    
    print("\n==== Farmer Notification =====")
    print(f"to: {farmer_phone}")
    print(f"Message: {message}")
    print("===============================\n")
    
    return {
        "success": True,
        "message": message
    }
    
    