import json
import rtmidi
import requests
import time

# Define the ESP8266 IP address
ESP8266_IP = "192.168.8.101"  # Replace this with your ESP8266's IP address

# Define the base URL
BASE_URL = f"http://{ESP8266_IP}/"
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




# Function to make a request to start the rainbow effect
def start_rainbow_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "rainbow"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the color wipe effect
def start_colorwipe_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "colorwipe"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the theater chase effect
def start_theaterchase_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "theaterchase"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the rainbow chase effect
def start_rainbowchase_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "rainbowchase"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the white strobe effect
def start_whitestrobe_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "whitestrobe"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to clear the lights
def clear_lights():
    url = BASE_URL + "setEffect"
    params = {"effect": "clearlights"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the color fade effect
def start_colorfade_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "colorfade"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the sparkle effect
def start_sparkle_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "sparkle"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the meteor rain effect
def start_meteorrain_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "meteorrain"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the twinkle effect
def start_twinkle_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "twinkle"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the color wipe reverse effect
def start_colorwipereverse_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "colorwipereverse"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the theater chase rainbow effect
def start_theaterchaserainbow_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "theaterchaserainbow"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the confetti effect
def start_confetti_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "confetti"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the sinelon effect
def start_sinelon_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "sinelon"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the juggle effect
def start_juggle_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "juggle"}
    response = requests.get(url, params=params)
    print(response.text)

