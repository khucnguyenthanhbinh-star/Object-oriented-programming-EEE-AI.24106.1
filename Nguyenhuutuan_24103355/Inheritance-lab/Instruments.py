def play_instruments(instruments):
    instruments.play()
class Guitar:
    def play(self):
        print("playing the guitar")
class Piano:
    def play(self):
        print("playing the piano")
guitar = Guitar()
play_instruments(guitar)
piano = Piano()
play_instruments(piano)