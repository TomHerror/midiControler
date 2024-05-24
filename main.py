from src.midi import Midi
import mido
import time
import dearpygui.dearpygui as dpg
from src.gui.synthGUI import SynthGui
import dearpygui.demo as demo


midi = Midi()
synthGui = SynthGui()

dpg.create_context()
dpg.create_viewport(title='midiController')

synthGui.render(midi)

# demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.start_dearpygui()
# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    dpg.render_dearpygui_frame()
dpg.destroy_context()

