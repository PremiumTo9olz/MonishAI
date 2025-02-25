import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

RAPIDAPI_KEY = "f8e9d3b73bmsh2634550ec0488d9p178362jsn8c21ee9ef13e"
RAPIDAPI_HOST = "gemini-pro-ai.p.rapidapi.com"

@app.route('/get_deal', methods=['POST'])
def get_deal():
    data = request.get_json()
    client_name = data.get("client_name", "Client")
    business_type = data.get("business_type", "Business")

    url = "https://your-api-name.p.rapidapi.com/your-endpoint"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST,
        "Content-Type": "application/json"
    }

    payload = {
        "input": f"Generate a sales pitch for {client_name} in {business_type}."
    }

    response = requests.post(url, json=payload, headers=headers)

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
