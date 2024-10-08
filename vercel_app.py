import sys
print(f"Python version: {sys.version}")
print(f"Python path: {sys.path}")

from app import app

# 这行很重要，它告诉 Vercel 如何运行应用
app = app

if __name__ == '__main__':
    app.run()