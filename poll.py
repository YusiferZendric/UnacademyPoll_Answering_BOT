import pyautogui as pt 
from time import sleep

option = input("Quickly Select a,b,c or d: ")
sleep(2)
while True:
	position = pt.locateOnScreen(f"{option.lower()}.png", confidence=0.7)
	print(position)
	pt.click(position)
