from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message').lower()  # Convert to lowercase for easier comparisons

    # Handle user inputs
    if any(word in user_message for word in ["hello", "hi"]):
         response = (
            "How may I assist you today?\n\n"
            "1. Product Recommendations\n\n"
            "2. Track Order\n\n"
            "3. Contact Support\n\n"
            "4. FAQs"
        )

    elif "product recommendations" in user_message or "1" == user_message:
        response = "Here are some product categories I can help with: Laptops, Mobile Phones. Please specify."
    elif "laptop" in user_message:
        response = (
            "Here are some laptop recommendations:\n\n"
            "1.HP 15s-du2095TU – Intel Core i3, 4GB RAM, 256GB SSD\n\n"
            "2.Dell Inspiron 3501 – 11th Gen Intel Core i3, 8GB RAM, 256GB SSD\n\n"
            "3.Acer Aspire 3 A315-23 – AMD Ryzen 3, 8GB RAM, 256GB SSD\n\n"
            "4.Lenovo IdeaPad Slim 3 – Intel Pentium Silver, 8GB RAM, 512GB SSD\n\n"
            "5.Asus VivoBook 15 X512DA – AMD Ryzen 5, 8GB RAM, 256GB SSD\n\n"
            "Would you like more information about any of these?"
        )
    elif "phone" in user_message:
        response = (
            "Here are some Mobile phone recommendations:\n\n"
            "1. iPhone 14\n\n"
            "2. Samsung Galaxy S23\n\n"
            "3. OnePlus 11\n\n"
            "4. Google Pixel 7\n\n"
            "Would you like details on any of these phones?"
        )   
    elif "track order" in user_message or "2" == user_message:
        response = "Your order #12345 is currently in transit and is expected to arrive on Dec 20th."
    elif "contact support" in user_message or "3" == user_message:
        response = "You can contact support at support@chatbot.com or call +123456789."
    elif "faqs" in user_message or "4" == user_message:
        response = "Here are some FAQs:\n\n1. Return policy\n\n2. Shipping \n\n3. Payment options."
    elif "return policy" in user_message:
        response = "You can initiate a return by visiting the Returns section in your account or contacting our support team."
    elif "shipping" in user_message:
        response = "We offer free shipping on orders over Rs.1500. Standard shipping takes 5-7 business days"
    elif "payment options" in user_message:
        response = "We accept UPI payments and Cash on delivery."        
    else:
        response = "I'm sorry, I didn't understand that. Can you rephrase your question?"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
