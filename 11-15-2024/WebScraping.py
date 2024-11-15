

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()

def navigazione_wikipedia(driver):
    driver.get("https://www.wikipedia.org/")
    time.sleep(5)
    search_bar = driver.find_element(By.ID, "searchInput")
    search_bar.send_keys("Python (programming language)"+ Keys.RETURN)
    time.sleep(3)
    elemento = driver.find_element()
    print(driver.title)
    print("Navigazione completata.")
    time.sleep(2)
    driver.quit()
    
navigazione_wikipedia(driver)
