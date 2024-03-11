from flask import Flask, request, jsonify, render_template
from src.chatbot import OpenAIChat

app = Flask(__name__, template_folder='templates')

chatbot = OpenAIChat()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message', '')

    # Generate response from chatbot
    bot_response = chatbot.generate_response(user_message)

    return jsonify({'message': bot_response})  # Return bot response as JSON


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)