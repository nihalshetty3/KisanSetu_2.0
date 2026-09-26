# KisanSetu_2.0
# 🌾 KisanSetu

KisanSetu is a **voice-first agricultural marketplace** that connects farmers directly with buyers while allowing farmers with basic phones to participate without needing a smartphone or complex application.

## 🚀 How It Works

```text
Farmer
   │
   │ Voice Listing
   ▼
Vapi Voice Agent
   │
   ▼
KisanSetu Backend
   │
   ▼
Crop Marketplace
   │
   ▼
Buyer Places Bid
   │
   ▼
Farmer Receives SMS
   │
   ├── 1 → Accept
   ├── 2 → Reject
   └── 3 → Wait
   │
   ▼
Bid Status Updated



## Workflow completed till date

                 KisanSetu
                     │
                     ▼
              FARMER VOICE
                     │
                     ▼
             Crop Listing API
                     │
                     ▼
              Crop stored
                     │
                     ▼
              BUYER MARKETPLACE
                     │
                     ▼
                View Crops
                     │
                     ▼
                 Place Bid
                     │
                     ▼
              Bid Created
                     │
                     ▼
            crop_id identifies
                 the crop
                     │
                     ▼
             farmer_id / phone
                     │
                     ▼
              SMS Notification
                     │
                     ▼
                  FARMER
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
          1          2          3
       ACCEPT      REJECT      WAIT

       
