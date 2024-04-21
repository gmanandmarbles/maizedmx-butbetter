import requests
import time

# Define the ESP8266 IP address
ESP8266_IP = "10.0.0.188"  # Replace this with your ESP8266's IP address

# Define the base URL
BASE_URL = f"http://{ESP8266_IP}/"

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

# Function to make a request to start the reverse color wipe effect
def start_colorwipereverse_effect():
    url = BASE_URL + "setEffect"
    params = {"effect": "colorwipereverse"}
    response = requests.get(url, params=params)
    print(response.text)

# Function to make a request to start the rainbow theater chase effect
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


start_whitestrobe_effect()
start_whitestrobe_effect()


# Call each function to start the corresponding effect
start_rainbow_effect()
time.sleep(5)  # Wait for 5 seconds before starting the next effect

start_colorwipe_effect()
time.sleep(5)

start_theaterchase_effect()
time.sleep(5)

start_rainbowchase_effect()
time.sleep(5)

start_whitestrobe_effect()
time.sleep(5)

clear_lights()
time.sleep(5)

start_colorfade_effect()
time.sleep(5)

start_sparkle_effect()
time.sleep(5)

start_meteorrain_effect()
time.sleep(5)

start_twinkle_effect()
time.sleep(5)

start_colorwipereverse_effect()
time.sleep(5)

start_theaterchaserainbow_effect()
time.sleep(5)

start_confetti_effect()
time.sleep(5)

start_sinelon_effect()
time.sleep(5)

start_juggle_effect()

