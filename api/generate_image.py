from http.server import BaseHTTPRequestHandler
from openai import OpenAI
import os
import json
from typing import Dict, Any

# 添加调试信息
print("环境变量：", os.environ)
print("OPENAI_API_KEY:", os.environ.get("OPENAI_API_KEY"))

# 尝试从不同的位置获取API密钥
api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY") or "your-default-api-key"

# 创建OpenAI客户端
client = OpenAI(api_key=api_key)

def generate_image(prompt: str) -> Dict[str, Any]:
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return {"image": response.data[0].url}
    except Exception as e:
        return {"error": str(e)}

def handler(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            result = generate_image(data['prompt'])
            return {
                "statusCode": 200,
                "body": json.dumps(result),
                "headers": {
                    "Content-Type": "application/json"
                }
            }
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON"}),
                "headers": {
                    "Content-Type": "application/json"
                }
            }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"}),
            "headers": {
                "Content-Type": "application/json"
            }
        }