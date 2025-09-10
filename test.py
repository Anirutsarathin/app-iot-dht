import requests
import json

# ตั้งค่า API URL
FIREBASE_PROJECT_ID = "dht22-5fa21"
DATE_TO_QUERY = "2025-02-02"
URL = f"https://firestore.googleapis.com/v1/projects/{FIREBASE_PROJECT_ID}/databases/(default)/documents/sensor/history/{DATE_TO_QUERY}"

# ส่ง HTTP GET Request
response = requests.get(URL, headers={"Content-Type": "application/json"})

# แสดงผลข้อมูล
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
