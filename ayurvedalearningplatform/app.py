from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure templates/index.html exists

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = get_bot_response(user_message)
    return jsonify({"reply": reply})

def get_bot_response(message):
    msg = message.lower()

    # Greetings
    if re.search(r"\b(hi|hello|hey|namaste|hii)\b", msg):
        return "Namaste! I'm your Ayurveda guide 🤝. Ask me about remedies, yoga, herbs, or doshas."

    # About Ayurveda
    elif "what is ayurveda" in msg or "about ayurveda" in msg:
        return ("Ayurveda is an ancient Indian system of natural healing. It balances the three doshas—Vata, Pitta, and Kapha—for health and wellness.")

    # Dosha explanation
    elif "dosha" in msg:
        return ("There are 3 main doshas:\n"
                "- Vata (Air & Space): Controls movement\n"
                "- Pitta (Fire & Water): Controls digestion\n"
                "- Kapha (Earth & Water): Controls structure\n"
                "Balance is the key to good health.")

    # Headache remedy
    elif "headache" in msg:
        return ("For headache relief, apply a paste of sandalwood or ginger on the forehead.\n"
                "You can also practice Shavasana and drink Tulsi tea.")

    # Fever
    elif "fever" in msg:
        return ("Try Tulsi tea, giloy juice, and stay hydrated. Ayurveda recommends rest and light food like khichdi.")

    # Cold
    elif "cold" in msg:
        return ("Inhale steam with eucalyptus oil, drink warm turmeric milk, and avoid cold food.")

    # Constipation
    elif "constipation" in msg:
        return ("Triphala powder at night with warm water is a great remedy. Also, eat fiber-rich fruits and practice yoga.")

    # Acidity
    elif "acidity" in msg:
        return ("Drink coconut water and avoid spicy foods. Amla juice or aloe vera can help soothe your stomach.")

    # Yoga suggestions
    elif "yoga" in msg or "asana" in msg:
        return ("Yoga promotes balance. Try:\n- Anulom Vilom (breathing)\n- Surya Namaskar\n- Pawanmuktasana (for digestion)\nWould you like yoga for a specific problem?")

    # Herbs
    elif "herbs" in msg or "herbal" in msg:
        return ("Popular Ayurvedic herbs:\n- Ashwagandha: stress relief\n- Triphala: digestion\n- Giloy: immunity booster\n- Brahmi: brain tonic\nAsk about a herb for more details.")

    # Thanks / exit
    elif "thank" in msg or "bye" in msg:
        return "You're welcome! Stay healthy and balanced with Ayurveda 🌿."

    # Fallback
    else:
        return ("I'm still learning. You can ask about:\n"
                "- Remedies for common problems\n"
                "- Yoga suggestions\n"
                "- Dosha explanation\n"
                "- Herbal uses\n"
                "Type 'what is Ayurveda' to get started!")

if __name__ == "__main__":
    app.run(debug=True)

