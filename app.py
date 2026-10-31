from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/')
def home():
    unused_message = "intentional Sonar finding"
    return jsonify({"message": "Hello from Docker!"})

@app.route('/health')
def health():
    unused_status = "intentional Sonar finding"
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
