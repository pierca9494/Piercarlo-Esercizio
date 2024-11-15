

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()

def navigazione_wikipedia(driver):
    driver.get("https://www.wikipedia.org/")
    time.sleep(3)
    search_bar = driver.find_element_by_id("searchInput")
    search_bar.send_keys("Python (programming language)")
    search_bar.send_keys(Keys.ENTER)
    time.sleep(3)
    print("Navigazione completata.")
    
navigazione_wikipedia()