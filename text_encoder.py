import numpy as np

class TextEncoder:
    def __init__(self):
        self.word_to_index = {}

    def fit(self, sentences):
        words = set()
        for sentence in sentences:
            for word in sentence.lower().split():
                words.add(word)
        self.word_to_index = {word: i for i, word in enumerate(sorted(words))}

    def transform(self, sentence):
        vector = np.zeros(len(self.word_to_index))
        for word in sentence.lower().split():
            if word in self.word_to_index:
                idx = self.word_to_index[word]
                vector[idx] = 1
        return vector
