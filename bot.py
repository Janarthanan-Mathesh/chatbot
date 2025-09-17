from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello! Chatbot is running on Azure 🚀"

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("text")
    response = f"You said: {user_input}"
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
