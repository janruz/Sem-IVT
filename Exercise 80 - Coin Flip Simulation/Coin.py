from random import randint

class Coin:

    _outcomes = {
        0: "H", # head
        1: "T" # tail
    }

    def flip(self):
        return self._outcomes[randint(0, 1)]