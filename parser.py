from xml.parsers.expat import model


def parse_message(message_dict):
    if not isinstance(message_dict, dict):
        return ""
    return message_dict.get("message") or message_dict.get("text", "")  

def classify_issue(message):
    message = message.lower()
    if "refund" in message or "charged" in message or "payment" in message:
        return "Billing"
    elif "crash" in message or "error" in message or "not working" in message:
        return "Technical Support"
    elif "buy" in message or "product" in message or "price" in message:
        return "Product Inquiry"
    elif "password" in message or "login" in message or "account" in message:
        return "Account/Login Issues"
    elif "suggestion" in message or "feedback" in message or "idea" in message:
        return "Feedback/Suggestions"
    elif "return" in  message or "replacement" in message or "exchange" in message:
        return "Return/Exchange"
    else:
        return "Uncategorized"
        
