from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()







driver.get("https://www.w3schools.com/html/html_tables.asp")


table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "table:nth-of-type(1)"))
)


rows = table.find_elements(By.TAG_NAME, "tr")


print("Contenuti Tabella:")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    print(", ".join(row_data))
    
time.sleep(2)


driver.quit()