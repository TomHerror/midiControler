from src.midi import Midi
import mido
import time
import dearpygui.dearpygui as dpg
from src.gui.synthGUI import SynthGui

midi = Midi()
synthGui = SynthGui()

dpg.create_context()
dpg.create_viewport(title='midiController')

synthGui.render(midi)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

