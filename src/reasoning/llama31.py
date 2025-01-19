import sys, os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from utils import _set_env

_set_env("NVIDIA_API_KEY")

client = ChatNVIDIA(
  model="meta/llama-3.1-405b-instruct",
  #api_key="$API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC", 
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
)

for chunk in client.stream([{"role":"user","content":"Write a limerick about the wonders of GPU computing."}]): 
  print(chunk.content, end="")
