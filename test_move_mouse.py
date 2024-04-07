import random
import pyautogui

for i in range(50):
    random_x = random.randint(-100, 100)
    random_y = random.randint(-100, 100)
    pyautogui.moveRel(random_x, random_y, 0.2, pyautogui.easeInOutQuad)
    print(pyautogui.position())
