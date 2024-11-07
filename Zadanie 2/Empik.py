from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_empik(driver):
    driver.get('https://www.empik.com/')
    driver.maximize_window()
    assert driver.current_url == "https://www.empik.com/", "URL strony nie jest poprawny"
    time.sleep(1)

    assert "Empik" in driver.title, "Tytuł strony nie zawiera 'Empik'"

    header = driver.find_element(By.TAG_NAME, "header")
    assert header.is_displayed(), "Nagłowek nie jest widoczny"

    try:
        przycisk = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-18n58r"))
        )
        assert przycisk.is_displayed()
        assert przycisk.is_enabled()
        przycisk.click()
        print("Cookies zaakceptowane")
    except Exception as e:
        print("Nie znaleziono przycisku akceptacji cookies:", e)

    time.sleep(1)

    pole_wyszukiwania = driver.find_element(By.CLASS_NAME, "css-1sobvo3")
    assert pole_wyszukiwania.is_displayed(), "Pole wyszukiwania nie jest widoczne"
    pole_wyszukiwania.send_keys("Ostatnie życzenie. Wiedźmin. Tom 1")
    pole_wyszukiwania.send_keys(Keys.RETURN)
    time.sleep(2)

    try:
        pierwszy_element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-list-item.js-reco-product a.seoTitle"))
        )
        pierwszy_element.click()

    except Exception as e:
        print("Błąd podczas klikania w pierwszy element:", e)
    time.sleep(1)

    obrazek = driver.find_element(By.TAG_NAME, "img")
    assert obrazek.is_displayed(), "Strona po wyszukiwaniu nie zawiera obrazku"

    assert "Opis produktu" in driver.page_source, "Opis produktu nie jest widoczny"

    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) > 0, "Brak linków na stronie"




for browser in [webdriver.Chrome,webdriver.Edge,webdriver.Firefox]:
    driver = browser()
    try:
        test_empik(driver)
        print(f"Test zakończony pomyślnie w {driver.name}")
    finally:
        driver.quit()
