from flask import Flask, request, jsonify
from service_req import handle_incoming_message

app = Flask(__name__)

@app.route("/receive", methods=["POST"])
def receive():
    data = request.json
    handle_incoming_message(data)
    return jsonify({"status": "processed"}), 200
