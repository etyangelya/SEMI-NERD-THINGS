import pyautogui
import time
import random

# Move the mouse slightly every few minutes to keep YouTube active
def prevent_youtube_idle():
    print("Anti-idle script started. Press Ctrl + C to stop.")
    try:
        while True:
            # Wait between 5 and 10 minutes randomly (simulate natural behavior)
            wait_time = random.randint(300, 600)
            time.sleep(wait_time)

            # Move the mouse by a small amount and back
            x, y = pyautogui.position()
            pyautogui.moveTo(x + 2, y + 2, duration=0.2)
            pyautogui.moveTo(x, y, duration=0.2)

            print(f"Activity sent at {time.strftime('%H:%M:%S')} (next in {wait_time//60} min)")
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    prevent_youtube_idle()
