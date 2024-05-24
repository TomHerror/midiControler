import dearpygui.dearpygui as dpg
from src.midi import Midi

class SynthGui:

    def render(self, midi: Midi):
        with dpg.window(label="midi"):
            dpg.add_text('midi outputs')
            dpg.add_combo(midi.ports)