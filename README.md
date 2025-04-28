# XORION-AI-
Customer Service Chatbot

This is a simple customer service chatbot built with Python, Flask, and NLTK. It handles basic customer queries such as return policies and order tracking.
Setup Instructions

    Clone the Repository:
    bash

    git clone <your-repository-url>
    cd customer-service-chatbot

    Create a Virtual Environment:
    bash

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install Dependencies:
    bash

    pip install -r requirements.txt

    Run the Application:
    bash

    python app.py

    Test the Chatbot: Use a tool like Postman or curl to send POST requests to http://localhost:5000/chat with a JSON body:
    json

    {"message": "What is your return policy?"}

Troubleshooting

    NLTK Data Download Error: If you encounter an error like [nltk_data] Error loading punkt, ensure you have an active internet connection. The app will attempt to download the 'punkt' tokenizer automatically. If the issue persists, manually download the data by running:
    python

    import nltk
    nltk.download('punkt')

    Flask Development Server Warning: The message WARNING: This is a development server is normal when running in debug mode. For production, use a WSGI server like Gunicorn:
    bash

    pip install gunicorn
    gunicorn -w 4 -b 0.0.0.0:5000 app:app

Project Structure

    app.py: Main application file containing the chatbot logic and Flask server.

    requirements.txt: Lists the required Python packages.

    README.md: Project documentation.

Contributing

Feel free to fork this repository and submit pull requests for improvements.
License

MIT License
