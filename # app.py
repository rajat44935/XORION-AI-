# app.py
from flask import Flask, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections
import os
import json

app = Flask(__name__)

# Function to ensure NLTK data is downloaded
def download_nltk_data():
    try:
        # Check if punkt data exists
        if not os.path.exists(os.path.join(nltk.data.find('tokenizers'), 'punkt')):
            nltk.download('punkt', quiet=True)
    except Exception as e:
        print(f"Failed to download NLTK data: {e}")

# Download NLTK data at startup
download_nltk_data()

# Define conversation pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! Welcome to our customer service. How can I assist you today?",]
    ],
    [
        r"what is your return policy",
        ["Our return policy allows returns within 30 days of purchase with a receipt. Would you like more details?",]
    ],
    [
        r"how can i track my order",
        ["You can track your order using the tracking number sent to your email. Would you like help finding it?",]
    ],
    [
        r"bye|goodbye",
        ["Thank you for contacting us. Have a great day!",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you please provide more details or ask another question?",]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400
        
        response = chatbot.respond(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
