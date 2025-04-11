from flask import Flask, request, jsonify
from service_req import handle_incoming_message

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Customer Support Classifier API is running!"})

@app.route("/classify", methods=["POST"])
def classify():
    try:
        data = request.get_json()
        handle_incoming_message(data)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)