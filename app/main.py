

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Configuration du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplace par ["http://localhost:5173"] pour restreindre aux clients autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_URL = "https://api-eu.vusion.io/vcloud/v1/stores/{store_id}/items/files/{file_name}"
API_KEY = "YOUR_SUBSCRIPTION_KEY"
AUTH_TOKEN = "Bearer YOUR_ACCESS_TOKEN"

@app.post("/upload/{store_id}")
async def upload_file(store_id: str, file: UploadFile = File(...)):
    url = API_URL.format(store_id=store_id, file_name=file.filename)
    headers = {
        "Content-Type": "application/octet-stream",
        "Cache-Control": "no-cache",
        "Ocp-Apim-Subscription-Key": API_KEY,
    }

    response = requests.post(url, data=file.file, headers=headers)
    
    print("Response status", response.json())

    if response.status_code == 200:
        return {"message": "Fichier envoyé avec succès", "correlationId": response.json().get("correlationId")}
    else:
        return {"error": response.json().get("message", "Une erreur est survenue"), "code": response.status_code}
