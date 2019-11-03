from Coin import Coin

class FlipSimulator:

    def __init__(self, coin: Coin):
        self.coin = coin

    def seek_consecutive_flips(self, number): # number = number of consecutive flips
        counter = 1
        last_flip_outcome = ""

        while counter != number:
            outcome = self.coin.flip()

            if last_flip_outcome == outcome:
                counter += 1
            else:
                counter = 1

            last_flip_outcome = outcome
            yield outcome