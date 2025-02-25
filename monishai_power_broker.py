import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load API credentials from Railway environment variables
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "open-ai21.p.rapidapi.com"

@app.route('/get_deal', methods=['POST'])
def get_deal():
    data = request.get_json()
    user_text = data.get("text", "Hello")

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

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "API call failed", "status": response.status_code}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
