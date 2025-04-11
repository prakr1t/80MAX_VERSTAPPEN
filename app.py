from flask import Flask, request, jsonify
from service_req import handle_incoming_message
from flask import request, jsonify
from service_req import handle_incoming_message

app = Flask(__name__)

@app.route("/", methods=["GET"])

def home():
    return jsonify({"message": "Customer Support Classifier API is running!"})


@app.route("/classify", methods=["POST"])

def classify():
    try:
        if not request.is_json:
            return jsonify({
                "status": "error",
                "message": "Request content type must be application/json"
            }), 400

        data = request.get_json()

        if data is None:
            return jsonify({
                "status": "error",
                "message": "No JSON data received"
            }), 400

        print("✅ Received data:", data)

        ticket = handle_incoming_message(data)

        return jsonify({
            "status": "success",
            "ticket": ticket
        }), 200

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)