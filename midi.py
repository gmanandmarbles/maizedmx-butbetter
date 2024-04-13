import json
import rtmidi

def save_to_json(data):
    with open('midi_actions.json', 'w') as f:
        json.dump(data, f)

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
    devices = {}
    for i in ports:
        devices[midiin.getPortName(i)] = i
    print("Available MIDI Input Ports:")
    for device_name, device_id in devices.items():
        print(f"{device_id}: {device_name}")
    
    selected_device_id = int(input("Enter the number corresponding to the MIDI input port: "))
    if selected_device_id in devices.values():
        print(f"Opening port {selected_device_id}: {midiin.getPortName(selected_device_id)}")
        midiin.openPort(selected_device_id)
    else:
        print("Invalid port number selected.")
        exit()
    
    actions = {}

    while True:
        m = midiin.getMessage(250) # some timeout in ms
        if m:
            if m.isNoteOn() or m.isNoteOff():
                decimal_note = m.getNoteNumber()
                note_name = note_name_from_decimal(decimal_note)
                action_value = input(f"Enter the function name for {note_name}: ")
                actions[note_name] = action_value
                save_to_json(actions)
            elif m.isController():
                print('CONTROLLER', m.getControllerNumber(), m.getControllerValue())
else:
    print('NO MIDI INPUT PORTS!')

