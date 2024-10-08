from http.server import BaseHTTPRequestHandler
from openai import OpenAI
import os
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

# 创建OpenAI客户端
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_image(prompt: str):
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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image_route():
    data = request.json
    result = generate_image(data['prompt'])
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Vercel需要这个handler函数
def handler(request):
    with app.request_context(request):
        return app.full_dispatch_request()