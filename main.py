import pyautogui
from pynput.mouse import Button, Controller
import keyboard
import time
mouse = Controller()
def aimandclicky(moveToX, moveToY):
    mouse.position = (moveToX, moveToY)
    mouse.click(Button.left, 1)
    time.sleep(0.1)
def IsItOnScreen():
    while True:
        while keyboard.is_pressed('q'):
                try:
                    button7location = pyautogui.locateOnScreen('Capture.PNG',grayscale=True, confidence=0.9)
                    button7location = pyautogui.center(button7location)
                    print(f'image found {button7location}')
                    aimandclicky(button7location[0],button7location[1])

                except TypeError:
                    print('cant find the image man')

IsItOnScreen()


