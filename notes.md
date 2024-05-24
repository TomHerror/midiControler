# print outputs

`[print(x) for x in mido.get_output_names()]`

# ouvertur port midi out

`outport = mido.open_output('PORT MIDI')`

# utiliser port midi out, send note, stop note, panic

`outport.send(mido.Message('note_on', channel=3, note=70, velocity=127))`
`outport.send(mido.Message('note_off', channel=3, note=70))`

a noter: pour chaque note penser a note_off sinon elle ne s'eteint jamais, en cas d'oublis pour tout eteindre sur le port utiliser:
`outport.panic()`


