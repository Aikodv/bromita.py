import pyautogui
import time

time.sleep(5)

with open("guion.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        
        mensaje = linea
        pyautogui.typewrite(mensaje, interval=0.00001)  
        pyautogui.press('enter')
        print("Línea leída:", mensaje)
