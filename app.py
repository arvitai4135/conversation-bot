# Placeholder for app.py
from flask import Flask, request, jsonify
from chatbot.chain import generate_response
from utils.logger import log_request_response
from utils.response_formatter import polish_response

app = Flask(__name__)

@app.route("/api/v1/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Empty input"}), 400

    try:
        raw_response = generate_response(user_input)
        final_response = polish_response(raw_response)
        log_request_response(user_input, final_response)

        return jsonify({"response": final_response})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route('/')
def test():
    return "Welcome the Arvitai technology"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5051)
