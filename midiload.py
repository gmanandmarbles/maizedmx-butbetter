import json
import rtmidi

def load_from_json():
    try:
        with open('midi_actions.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: midi_actions.json file not found.")
        return {}

def get_function_name(midi_data, actions):
    if midi_data.isNoteOn() or midi_data.isNoteOff():
        decimal_note = midi_data.getNoteNumber()
        note_name = note_name_from_decimal(decimal_note)
        if note_name in actions:
            return actions[note_name]
    elif midi_data.isController():
        controller_number = midi_data.getControllerNumber()
        controller_value = midi_data.getControllerValue()
        controller_key = f"CONTROLLER {controller_number} {controller_value}"
        if controller_key in actions:
            return actions[controller_key]
        else:
            controller_key = f"CONTROLLER {controller_number}"
            if controller_key in actions:
                return actions[controller_key]
    return "BUTTON NOT INITIALIZED"

def note_name_from_decimal(decimal_note):
    # Converts decimal MIDI note to its corresponding note name
    note_number = int(decimal_note)
    octave = (note_number // 12) - 1
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_name = note_names[note_number % 12]
    return f"{note_name}-{octave}"

midiin = rtmidi.RtMidiIn()

ports = range(midiin.getPortCount())
if ports:
    for i in ports:
        print(midiin.getPortName(i))
    print("Opening port 0!")
    midiin.openPort(0)
    
    actions = load_from_json()

    while True:
        m = midiin.getMessage(250) # some timeout in ms
        if m:
            function_name = get_function_name(m, actions)
            print("Function name:", function_name)
else:
    print('NO MIDI INPUT PORTS!')

