import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()

# Control variables
running = False
toggle_key = KeyCode(char='b')
quit_key = KeyCode(char='p')  # 'P' key

def worker():
    """Holds down left mouse button and presses 'E' every 5 seconds while running."""
    global running
    mouse.press(Button.left)
    print("Left mouse button held down.")
    while running:  
        time.sleep(1)
        if not running:
            break
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        print("Pressed and released 'E'.")
    mouse.release(Button.left)
    print("Stopped and released left mpouse button.")

def on_press(key):
    global running
    if key == toggle_key:
        if not running:
            running = True
            threading.Thread(target=worker, daemon=True).start()
        else:
            running = False
    elif key == quit_key:
        print("Exiting program.")
        return False  # stop listener

def main():
    print("Press 'b' to start/stop holding. Press 'esc' to quit.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
