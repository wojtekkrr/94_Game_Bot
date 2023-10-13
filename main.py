import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import keyboard


url = "https://elgoog.im/t-rex/"

# Adres sterownika
chrome_driver_path = "C:\development\chromedriver.exe"

# Nie wyłączanie okna po zakończeniu skryptu
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Wczytanie sterownika
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Maksymalizuj okno przeglądarki na pełen ekran
driver.maximize_window()

# Adres strony z której będą zczytywane dane
driver.get(url)

sleep(2)

pyautogui.press('space')

# Pobierz współrzędne myszy
# x, y = pyautogui.position()
#
# print(x)
# print(y)

# Współrzędne pixela do analizy
x = 555
y_jump = 741
y_hide = 641
y_low = 740

x_steps = 15
x_step = 1


kolor_poszukiwany = (83, 83, 83)

x_ckeck = []
for i in range(x_steps + 1):
    x_ckeck.append(int(x - x_steps/2 * x_step + i * x_step))

print(x_ckeck)


def action():
    for x_cord in x_ckeck:
        kolor_piksela_dol = pyautogui.pixel(x_cord, y_jump)
        kolor_piksela_gora = pyautogui.pixel(x_cord, y_hide)
        kolor_piksela_low = pyautogui.pixel(x_cord, y_low)
        if kolor_piksela_low != kolor_poszukiwany and kolor_piksela_gora == kolor_poszukiwany:
            pyautogui.press('down')
            print("teraz dol")
        if kolor_piksela_dol == kolor_poszukiwany:
            pyautogui.press('space')
            print("teraz gora")
            sleep(0.01)


# Pętla while będzie działać dopóki warunek escape_pressed będzie równy False
escape_pressed = False
while not escape_pressed:
    action()
    sleep(0.01)
    if keyboard.is_pressed('esc'):
        escape_pressed = True