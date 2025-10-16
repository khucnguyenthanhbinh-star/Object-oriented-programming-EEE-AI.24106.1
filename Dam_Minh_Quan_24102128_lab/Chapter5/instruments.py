def play_instrument(instrument):
	instrument.play()
class Guitar:
    def play(self):
        print("playing the guitar")
class Piano:
    def play(self):
        print("playing the piano")
guitar = Guitar()
play_instrument(guitar)
piano = Piano()
play_instrument(piano)

