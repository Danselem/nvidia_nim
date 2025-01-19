import requests, base64
import sys, os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from utils import _set_env

api_key = _set_env("NVIDIA_API_KEY")

invoke_url = "https://ai.api.nvidia.com/v1/vlm/microsoft/kosmos-2"

data_path = os.path.join(os.path.dirname(__file__), './data/family.jpg')
data_path = os.path.abspath(data_path)
with open(data_path, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"

headers = {
  "Authorization": "Bearer "+api_key,
  "Accept": "application/json"
}

payload = {
  "messages": [
    {
      "role": "user",
      "content": f'Who is in this photo? <img src="data:image/png;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 1024,
  "temperature": 0.20,
  "top_p": 0.20
}

response = requests.post(invoke_url, headers=headers, json=payload)

print(response.text)

print(response.json())
