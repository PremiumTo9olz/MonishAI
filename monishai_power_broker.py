import openai
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# AI-Generated Outreach Message

def generate_message(client_name, business_type):
    prompt = f"""
    Generate a high-converting outreach message for {business_type} to persuade {client_name} to close a high-ticket deal.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert sales negotiator."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

@app.route('/get_deal', methods=['POST'])
def get_deal():
    data = request.json
    client_name = data.get("client_name", "Client")
    business_type = data.get("business_type", "Business")
    
    message = generate_message(client_name, business_type)
    
    return jsonify({"outreach_message": message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
