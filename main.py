from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.rpa-unlimited.com/youtube/robocorp-tutorial/") 

driver.maximize_window()

driver.find_element(By.ID,"company-name").send_keys("Toms Tech Academy")

time.sleep(7)

driver.find_element(By.CLASS_NAME,"formkit-close").click()

time.sleep(2)

driver.find_element(By.ID,"company-contact").send_keys("Thomas")

time.sleep(2)

driver.execute_script("window.scrollTo(0, 500)")

time.sleep(5)

driver.find_element(By.CLASS_NAME,"btn-success").click()

time.sleep(5)

driver.quit