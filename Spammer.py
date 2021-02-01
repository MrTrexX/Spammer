import pyautogui
import random
import time

spams = ["Lets go", "yes", "haha", "yeet", "@the spammer posiedon"]

while True:
    pyautogui.typewrite(random.choice(spams))
    time.sleep(0.1)
    pyautogui.press("enter")
