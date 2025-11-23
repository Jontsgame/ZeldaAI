from flask import Flask, render_template, request
from model import ScratchAI

app = Flask(__name__)
ai = ScratchAI()
ai.load_model("trained_model.pkl")  # Modell laden

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/send", methods=["POST"])
def chat():
    user_msg = request.form["message"]
    response = ai.generate(start_words=user_msg.split(), max_words=30)
    return response

if __name__ == "__main__":
    app.run(debug=True)  # Website starten
