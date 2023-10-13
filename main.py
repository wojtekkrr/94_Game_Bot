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
x = 470
y = 690

kolor_poszukiwany = (83, 83, 83)

# Pętla while będzie działać dopóki warunek escape_pressed będzie równy False
escape_pressed = False
while not escape_pressed:
    kolor_piksela = pyautogui.pixel(x, y)
    # print(kolor_piksela)
    if kolor_piksela == kolor_poszukiwany:
        pyautogui.press('space')
    sleep(0.001)
    if keyboard.is_pressed('esc'):
        escape_pressed = True