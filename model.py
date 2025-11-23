import pickle
import random
import re

class ScratchAI:
    def __init__(self):
        self.model = {}  # (word1, word2) -> [word3, ...]
        self.end_punct = {'.', '!', '?'}

    def train(self, text, append=False):
        if not append:
            self.model = {}

        words = re.findall(r"\b\w+\b|[.!?]", text)
        for i in range(len(words) - 2):
            key = (words[i], words[i+1])
            next_word = words[i+2]
            if key not in self.model:
                self.model[key] = []
            self.model[key].append(next_word)

    def generate(self, start_words=None, max_words=30):
        # Smarter Startpunkt
        key = self._choose_start(start_words)
        result = [key[0], key[1]]

        for _ in range(max_words-2):
            next_words = self.model.get(key)
            if not next_words:
                break
            next_word = random.choice(next_words)
            result.append(next_word)
            key = (key[1], next_word)
            if next_word in self.end_punct:
                break
        return " ".join(result)

    def _choose_start(self, words):
        # Versuche wichtige Wörter aus der Frage zu finden
        important = [w.lower() for w in words if len(w) > 3]  # sehr simple Heuristik
        candidates = []
        for key in self.model.keys():
            if key[0].lower() in important or key[1].lower() in important:
                candidates.append(key)
        if candidates:
            return random.choice(candidates)
        else:
            return random.choice(list(self.model.keys()))

    def save_model(self, filepath="trained_model.pkl"):
        with open(filepath, "wb") as f:
            pickle.dump(self.model, f)

    def load_model(self, filepath="trained_model.pkl"):
        with open(filepath, "rb") as f:
            self.model = pickle.load(f)
