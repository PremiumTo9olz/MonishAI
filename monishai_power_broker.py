import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Default route to check if the server is running
@app.route('/')
def home():
    return "MonishAI Power Broker is running!"

# Load API credentials from Railway environment variables
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "open-ai21.p.rapidapi.com"

@app.route('/get_deal', methods=['POST'])
def get_deal():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Invalid request. 'text' field is required"}), 400

    user_text = data["text"]
    url = f"https://{RAPIDAPI_HOST}/conversationllama"
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Host": RAPIDAPI_HOST,
        "X-RapidAPI-Key": RAPIDAPI_KEY,
    }
    payload = {
        "messages": [{"role": "user", "content": user_text}],
        "web_access": False
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
