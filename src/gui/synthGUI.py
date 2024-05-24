import time
import mido
import dearpygui.dearpygui as dpg
from src.midi import Midi

class SynthGui:
    def __init__(self):
        self.selected = None
        self.midi = None

    def render(self, midi: Midi):
        self.midi = midi
        with dpg.window(label="midi output"):
            label = dpg.add_text('midi outputs')
            selected_midi_output = dpg.add_combo(
                items=self.midi.ports,
                callback=self.setMidiOutput)
            dpg.add_button(label='open sequencer',
                callback=self.openSequencer)
            dpg.add_button(label='refresh midi outputs',
                callback=self.refreshMidiOutputs)

    def setMidiOutput(self, sender, data, user_data):
        self.selected = data
    
    def refreshMidiOutputs(self, sender, data, user_data):
        self.midi.ports = mido.get_output_names()
    
    def openSequencer(self, sender, data, user_data):
        # faire un fichier sequenceur plus tard et le gerer la bas 
        with dpg.window(label='sequenceur'):
            sequenceur = dpg.add_button(label='send note',
                callback=self.sendNote)
    
    def sendNote(self, sender, data, user_data):
        outport = mido.open_output(self.selected)
        outport.send(mido.Message('note_on', channel=3, note=70, velocity=127))
        time.sleep(0.5)
        outport.send(mido.Message('note_off', channel=3, note=70))
