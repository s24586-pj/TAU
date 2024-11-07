from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_olx(driver):
    driver.get('https://www.olx.pl/')
    driver.maximize_window()
    assert driver.current_url == "https://www.olx.pl/", "URL strony nie jest poprawny"
    time.sleep(1)

    assert "Ogłoszenia" in driver.title, "Tytuł strony nie zawiera 'Ogłoszenia'"

    header = driver.find_element(By.TAG_NAME, "header")
    assert header.is_displayed(), "Nagłowek nie jest widoczny"

    try:
        przycisk = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        przycisk.click()
        print("Cookies zaakceptowane")
    except Exception as e:
        print("Nie znaleziono przycisku akceptacji cookies:", e)

    time.sleep(2)

    pole_wyszukiwania = driver.find_element(By.ID, "search")
    assert pole_wyszukiwania.is_displayed(), "Pole wyszukiwania nie jest widoczne"
    pole_wyszukiwania.send_keys("Pułapki myślenia - Daniel Kahneman")
    pole_wyszukiwania.send_keys(Keys.RETURN)
    time.sleep(2)

    assert "Pułapki myślenia" in driver.page_source, "Wyniki wyszukiwania nie zawierają 'Pułapki myślenia'"

    pierwszy_element_a = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class, 'css-z3gu2d')])[1]"))
    )
    pierwszy_element_a.click()

    time.sleep(5)

    obrazek = driver.find_element(By.TAG_NAME, "img")
    assert obrazek.is_displayed(), "Strona po wyszukiwaniu nie zawiera obrazku"

    stopka = driver.find_element(By.ID, "footerContent")
    assert stopka.is_displayed(), "Stopka nie jest widoczna"

    login = driver.find_element(By.LINK_TEXT, "Twoje konto")
    assert login.is_displayed(), "Przycisk 'Twoje konto' nie jest widoczny"
    login.click()
    time.sleep(2)

    assert "Zaloguj się" in driver.title, "Nie jesteś na stronie logowania"



for browser in [webdriver.Chrome, webdriver.Edge,webdriver.Edge]:
    driver = browser()
    try:
        test_olx(driver)
        print(f"Test zakończony pomyślnie w {driver.name}")
    finally:
        driver.quit()
