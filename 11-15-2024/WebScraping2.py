from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()




url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)

# Trova username e password nella pagina
username = driver.find_element(By.XPATH, "/html/body/div/div/section/section/ul/li[2]/b[1]").text
password = driver.find_element(By.XPATH, "/html/body/div/div/section/section/ul/li[2]/b[2]").text

# Inserisci i dati di login
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "submit")

username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()


time.sleep(2)


success_message = driver.find_element(By.TAG_NAME, "h1").text
print("Messaggio di successo:", success_message)

# Clicca sul pulsante di logout
logout_button = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/div/div/div/a")
logout_button.click()
time.sleep(2)
# Stampa il titolo della pagina corrente
print("Titolo della pagina:", driver.title)



driver.quit()
