import mido

class Midi:
    def __init__(self):
        self.ports = mido.get_output_names()