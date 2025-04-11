from flask import Flask, request, jsonify
from service_req import handle_incoming_message
from flask import request, jsonify
from service_req import handle_incoming_message

from categories import category_to_department
from parser import classify_issue, parse_message
from mock_input import incoming_message
from parser import parse_message
from categories import category_to_department


def map_to_department(category):
    return category_to_department.get(category, "general_support@company.com")

def create_service_request(category, sender, message):
    department = map_to_department(category)
    print(f"Ticket Created!")
    print(f"From: {sender}")
    print(f"Category: {category}")
    print(f"Assigned to: {department}")
    print(f"Message: {message}")
    print("="*40)

"""
def handle_incoming_message(message_dict):
    message = parse_message(message_dict)
    category = classify_issue(message)
    create_service_request(category, message_dict["sender"], message)

def handle_incoming_message(message_dict):
    message = parse_message(message_dict)
    category = classify_issue(message)
    create_service_request(category, message_dict["sender"], message)
"""


def handle_incoming_message(data):
    email = data.get("email")
    message = parse_message(data) 

    category = classify_issue(message) 
    print(f"[DEBUG] Category received: '{category}'")
    assigned_to = category_to_department.get(category, "general_support@company.com")

    ticket = {
        "from": email,
        "category": category,
        "assigned_to": assigned_to,
        "message": message
    }

    # Keep printing to terminal (for logs/debug)
    print("Ticket Created!")
    for k, v in ticket.items():
        print(f"{k.capitalize()}: {v}")
    print("=" * 30)

    return ticket

handle_incoming_message(incoming_message)




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