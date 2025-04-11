from categories import category_to_department
from parser import classify_issue, parse_message
from mock_input import incoming_message



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


def handle_incoming_message(message_dict):
    message = parse_message(message_dict)
    category = classify_issue(message)
    create_service_request(category, message_dict["sender"], message)

def handle_incoming_message(message_dict):
    message = parse_message(message_dict)
    category = classify_issue(message)
    create_service_request(category, message_dict["sender"], message)

handle_incoming_message(incoming_message)