
import json
import rtmidi

def load_from_json():
    try:
        with open('midi_actions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: midi_actions.json file not found.")
        return {}

actions = load_from_json()

def note_name_from_decimal(decimal_note):
    # Converts decimal MIDI note to its corresponding note name
    note_number = int(decimal_note)
    octave = (note_number // 12) - 1
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_name = note_names[note_number % 12]
    return f"{note_name}-{octave}"

def get_function_name(note_name):
    if note_name in actions:
        return actions[note_name]
    else:
        return "BUTTON NOT INITIALIZED"

def print_message(midi):
    if midi.isNoteOn() or midi.isNoteOff():
        decimal_note = midi.getNoteNumber()
        note_name = note_name_from_decimal(decimal_note)
        function_name = get_function_name(note_name)
        print("Function name:", function_name)
    elif midi.isController():
        print('CONTROLLER', midi.getControllerNumber(), midi.getControllerValue())

midiin = rtmidi.RtMidiIn()

ports = range(midiin.getPortCount())
if ports:
    for i in ports:
        print(midiin.getPortName(i))
    print("Opening port 0!")
    midiin.openPort(0)
    
    while True:
        m = midiin.getMessage(250) # some timeout in ms
        if m:
            print_message(m)
else:
    print('NO MIDI INPUT PORTS!')

