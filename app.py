from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input or "heyy" in user_input:
        return "oiii! How can I help you today?"
    elif "order status" in user_input or "status of my order" in user_input:
        return "To check your order status, please provide your order number"
    # Order Tracking
    elif "track my order" in user_input or "where is my order" in user_input:
        return "To track your order, please provide your tracking number."
    # Cancel Order
    elif "cancel my order" in user_input or "cancel order" in user_input:
        return "To cancel your order, please provide your order number. Note: Orders can only be canceled if they haven't been shipped yet."
    # Return Order
    elif "return my order" in user_input or "return policy" in user_input:
        return "Our return policy allows returns within 30 days of delivery. Please provide your order number to initiate a return."
    # Payment Issues
    elif "payment issue" in user_input or "payment failed" in user_input:
        return "If you're facing payment issues, please check your payment method or contact your bank. If the problem persists, provide your order number for further assistance."
    # Refund Status
    elif "refund status" in user_input or "where is my refund" in user_input:
        return "To check your refund status, please provide your order number. Refunds typically take 5-7 business days to process."
    # Change Shipping Address
    elif "change shipping address" in user_input or "update address" in user_input:
        return "To change your shipping address, please provide your order number and the new address. Note: Changes can only be made before the order is shipped."

    # Damaged or Missing Items
    elif "damaged item" in user_input or "missing item" in user_input:
        return "We apologize for the inconvenience. Please provide your order number and details about the issue (e.g., damaged or missing item) so we can assist you."
    # Contact Support
    elif "talk to a human" in user_input or "contact support" in user_input:
        return "Our customer support team is available 24/7. Please call +1-800-123-4567 or email support@example.com for assistance."
    # General Help
    elif "help" in user_input or "support" in user_input:
        return "How can I assist you today? You can ask about order status, tracking, returns, cancellations, or payment issues."
    elif "hate you" in user_input:
        return "love you"
    elif "love you" in user_input:
        return "I love you too"
    elif "miss you" in user_input:
        return "I miss you too❤️"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "iam bot"
    elif "what can you do" in user_input:
        return "I can chat with you, answer simple questions, and help you with basic tasks. Try asking me something!"
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    elif "date" in user_input:
        from datetime import datetime
        now = datetime.now()
        return f"Today's date is {now.strftime('%Y-%m-%d')}."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! 😊"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "weather" in user_input:
        return "I'm sorry, I don't have access to weather data right now."
    elif "joke" in user_input:
        return "உன்னை ஒரு நிமிஷம் பார்க்கிறேனே… அப்போதே என் இதயம் பீர்ன்னு கொதிக்குது! ❤️☕"
    else:
        return "I'm sorry, I don't understand that. Can you rephrase or ask something else?"

@app.route("/")
def index():
    print("Loaded HTML")  # This should print in your terminal
    return render_template("index.html")
  # ✅ must match templates/index.html

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.json["msg"]
    return jsonify({"response": get_bot_response(user_msg)})

if __name__ == "__main__":
    app.run(debug=True)
