import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import keyboard

# Adres strony z grą
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

# Początek gry
pyautogui.press('space')

# Współrzędne pixela do analizy
x = 550
y_jump = 710
y_hide = 641
y_low = 740

# Liczba pikseli do analizy w poziomie i ich odstęp
x_steps = 5
x_step = 1

kolor_poszukiwany = (83, 83, 83)

# Utworzenie linii pikseli, która jest sprawdzana
x_check = []
for i in range(x_steps + 1):
    x_check.append(int(x - x_steps / 2 * x_step + i * x_step))


# Wykonywanie akcji w zależności od dostrzeżonych przeszkód
def action():
    # Sprawdzania pikseli na różnych wysokościach, będących w jednej linii
    for x_cord in x_check:
        kolor_piksela_dol = pyautogui.pixel(x_cord, y_jump)
        kolor_piksela_gora = pyautogui.pixel(x_cord, y_hide)
        kolor_piksela_low = pyautogui.pixel(x_cord, y_low)
        # Jeśli na dole nie ma przeszkody, a wysoko jest, to pochyl się
        if kolor_piksela_low != kolor_poszukiwany and kolor_piksela_gora == kolor_poszukiwany:
            pyautogui.press('down')
            # Nie naciskaj przez chwilę klawiszy
            sleep(0.2)
            # Jeżeli przeszkoda nisko, to skocz
        if kolor_piksela_dol == kolor_poszukiwany:
            pyautogui.press('space')
            # Nie naciskaj przez chwilę klawiszy
            sleep(0.01)


# Pętla while będzie działać dopóki warunek escape_pressed będzie równy False
escape_pressed = False
while not escape_pressed:
    action()
    # Przerwy w sprawdzaniu
    sleep(0.005)
    if keyboard.is_pressed('esc'):
        escape_pressed = True
