# midiControlerGo
midi controler to learn go

# install tools

`sudo pacman -S jack2 a2jmidid`

`sudo pacman -S fluidsynth`

# configuration
## 1 configurer Jack et a2jmidid

lancer le serveur jack

`jack_control start`

Démarrez a2jmidid pour créer les connexions MIDI virtuelles

a2jmidid -e &

## 2 config FluidSynth

Lancez FluidSynth avec un SoundFont (par exemple, GeneralUser SoundFont) :

`fluidsynth -a jack -m alsa_seq /path/to/your/soundfont.sf2`

## 3 configurer les ports midi virtuels

Vous pouvez utiliser aconnect pour vérifier et gérer les connexions MIDI virtuelles. Par exemple :

```
aconnect -i  # List input ports
aconnect -o  # List output ports
```

