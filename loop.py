import time
import mido

outport = mido.open_output('CRAVE:CRAVE MIDI 1 24:0')

notes = [35, 45, 50, 60, 45, 55]

i = 0
while i < 10:
    for note in notes:
        outport.send(mido.Message('note_on', note=note))
        time.sleep(0.15)
        outport.send(mido.Message('note_off', note=note))
        time.sleep(0.05)
    i += 1

