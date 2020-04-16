import pyautogui
import time

time.sleep(5)

while True:

	button_points = pyautogui.locateOnScreen('box_points.png',confidence=0.8)

	if button_points is None:
		time.sleep(10)
	else:
		button_location = pyautogui.center(button_points)

		pyautogui.click(button_location)