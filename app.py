from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

# 如果您想在主应用中也处理 /generate-image 请求，可以添加以下路由
# 但请注意，这可能会与 Serverless 函数冲突
# @app.route('/generate-image', methods=['POST'])
# def generate_image():
#     # 处理图像生成的逻辑
#     pass

if __name__ == '__main__':
    app.run(debug=True)