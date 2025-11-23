from model import ScratchAI

def train_from_text(filepath="raw_data.txt", model_file="trained_model.pkl"):
    ai = ScratchAI()
    try:
        ai.load_model(model_file)
        append = True
        print("Altes Modell geladen – wir erweitern es.")
    except FileNotFoundError:
        append = False
        print("Neues Modell wird erstellt.")

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    ai.train(text, append=append)
    ai.save_model(model_file)
    print("Training abgeschlossen und Modell gespeichert!")

if __name__ == "__main__":
    train_from_text()
