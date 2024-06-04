import time
import pyautogui
from pynput import keyboard
import argparse

def on_press(key):
    global loop
    if key == keyboard.Key.delete:
        print("Exiting program...")
        pyautogui.keyUp(target_key)
        loop = False
        return False
    try:
        if key.char == args.start_key:
            pyautogui.keyDown(target_key)
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char == args.start_key:
            pyautogui.keyUp(target_key)
    except AttributeError:
        pass
if __name__ == "__main__":
    print("For start key and stop key, use one letter, number, or symbol only. No combinations")
    parser = argparse.ArgumentParser(description="Press target key when start key is pressed.")
    parser.add_argument("start_key", help="The key that triggers the start", type=str)
    parser.add_argument("target_key", help="The key to be pressed when start key is pressed", type=str)
    args = parser.parse_args()
    print("Press 'Delete' key to exit the program.")
    start_key = args.start_key
    target_key = args.target_key
    loop = True
    start = 0
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    while loop:
        time.sleep(0.1)
