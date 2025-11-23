from model import ScratchAI

ai = ScratchAI()
ai.load_model("trained_model.pkl")

print("KI bereit zum chatten! (exit zum beenden)")

while True:
    user = input("DU: ")
    if user.lower() == "exit":
        break

    words = user.split()
    response = ai.generate(start_words=words, max_words=30)
    print("KI:", response)
