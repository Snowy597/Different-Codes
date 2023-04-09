import os
import random
import base64
import time

# radio frequencies cuz im bored
def generate_radio_frequency():
    frequency = str(random.randint(10, 120)) + " MHz"
    return frequency

# generate base64 shite cuz why tf not
def generate_base64_string():
    text = os.urandom(16)
    base64_text = base64.b64encode(text).decode()
    return base64_text

# Loop this shit
while True:
    frequency = generate_radio_frequency()
    base64_text = generate_base64_string()
    print(frequency + ": " + base64_text)
    time.sleep(5) # it waits 5 seconds dipshit

    # HEIL HITLER