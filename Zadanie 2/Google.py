from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def test_accept_cookies(driver):
    driver.get("https://www.google.com")
    driver.maximize_window()

    try:
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "L2AGLb"))
        )
        accept_button.click()
    except Exception as e:
        print("Nie znaleziono przycisku akceptacji cookies:", e)

    assert "Google" in driver.title, "Strona nie zawiera 'Google'"

    pole_wyszukiwania = driver.find_element(By.NAME, "q")
    pole_wyszukiwania.send_keys("Selenium")
    pole_wyszukiwania.send_keys(Keys.RETURN)
    time.sleep(2)

    assert 'Selenium' in driver.page_source, "Wyniki wyszukiwania nie zawierają 'Selenium'"

    pierwszy_wynik = driver.find_element(By.XPATH, "//h3")
    assert pierwszy_wynik.is_displayed(), "Pierwszy wynik wyszukiwania nie jest widoczny"
    pierwszy_wynik.click()

    time.sleep(2)
    assert "Selenium" in driver.title, "Tytuł strony nie zawiera 'Selenium'"

    obrazek_selenium = driver.find_element(By.TAG_NAME, "img")
    assert obrazek_selenium.is_displayed(), "Strona Selenium nie zawiera obrazku"

    assert "Selenium" in driver.page_source, "Strona główna nie jest widoczna"

    navbar = driver.find_element(By.ID, "main_navbar")
    assert navbar.is_displayed(), "Navbar nie jest widoczny"

    footer = driver.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed(), "Footer nie jest widoczny"

    dokkumentacja = driver.find_element(By.LINK_TEXT, "Documentation")
    assert dokkumentacja.is_displayed(), "Przycisk do dokumentacji nie jest widoczny"

    dokkumentacja.click()
    time.sleep(2)


for browser in [webdriver.Chrome, webdriver.Firefox, webdriver.Edge]:
    driver = browser()
    try:
        test_accept_cookies(driver)
        print(f"Test zakończony pomyślnie w {driver.name}")
    finally:
        driver.quit()
