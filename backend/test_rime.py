import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("RIME_API_KEY")

url = "https://users.rime.ai/v1/rime-tts"

headers = {
    "Accept": "audio/wav",
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "text": "Hello! I am VoxTutor. Let's learn something together.",
    "speaker": "cupola",
    "modelId": "coda",
    "lang": "eng"
}

response = requests.post(
    url,
    headers=headers,
    json=data
)

print("STATUS:", response.status_code)
print("CONTENT TYPE:", response.headers.get("content-type"))

if response.ok:
    with open("backend/rime_test.wav", "wb") as f:
        f.write(response.content)

    print("🔥 RIME TEST SUCCESS!")
    print("Audio saved as backend/rime_test.wav")

else:
    print("❌ RIME ERROR:")
    print(response.text)