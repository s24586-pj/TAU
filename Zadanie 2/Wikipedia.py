from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_wikipedia(driver):
    driver.get('https://pl.wikipedia.org/wiki/Wikipedia:Strona_główna')
    driver.maximize_window()
    time.sleep(2)

    assert "Wikipedia" in driver.title, "Tytuł strony nie zawiera 'Wikipedia'"
    assert "Strona główna" in driver.page_source, "Strona główna nie jest widoczna"

    pole_wyszukiwania = driver.find_element(By.NAME, "search")
    assert pole_wyszukiwania.is_displayed(), "Pole wyszukiwania nie jest widoczne"

    pole_wyszukiwania.send_keys('Selenium')
    pole_wyszukiwania.send_keys(Keys.RETURN)
    time.sleep(2)

    assert 'Selenium' in driver.page_source, "Wyniki wyszukiwania nie zawierają Selenium"

    link_selenium = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
    assert link_selenium.is_displayed(), "Link do artykułu o Selenium nie jest widoczny"

    obrazek_selenium = driver.find_element(By.TAG_NAME, "img")
    assert obrazek_selenium.is_displayed(), "Strona wikipedii nie zawiera obrazku"

    stopka = driver.find_element(By.ID, "footer")
    assert stopka.is_displayed(), "Stopka nie jest widoczna"

    login = driver.find_element(By.LINK_TEXT, "Zaloguj się")
    assert login.is_displayed(), "Przycisk 'Zaloguj się' nie jest widoczny"

    login.click()
    time.sleep(2)

    assert "Zaloguj się" in driver.title, "Nie jesteś na stronie logowania"


for browser in [webdriver.Chrome, webdriver.Firefox, webdriver.Edge]:
    driver = browser()
    try:
        test_wikipedia(driver)
        print(f"Test zakończony pomyślnie w {driver.name}")
    finally:
        driver.quit()
