
import requests, base64
import sys, os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from utils import _set_env

# for model in ChatNVIDIA.get_available_models():
#     print(model)

api_key = _set_env("NVIDIA_API_KEY")


invoke_url = "https://ai.api.nvidia.com/v1/gr/meta/llama-3.2-90b-vision-instruct/chat/completions"
stream = True

data_path = os.path.join(os.path.dirname(__file__), './data/glimpsecls.png')
data_path = os.path.abspath(data_path)

with open(data_path, "rb") as f:
  image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"
  

headers = {
  "Authorization": "Bearer "+api_key,
  "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
  "model": 'meta/llama-3.2-90b-vision-instruct',
  "messages": [
    {
      "role": "user",
      "content": f'What is in this image? <img src="data:image/png;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 512,
  "temperature": 1.00,
  "top_p": 1.00,
  "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())
