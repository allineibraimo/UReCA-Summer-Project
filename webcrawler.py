from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\Drivers\chromedriver-win32\chromedriver.exe")

driver.get("https://www.thingiverse.com/")

# WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@id="sp_message_iframe_382445"]')))
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@title,'ACCEPT ALL')]"))).click()

time.sleep(600)

driver.find_element(By.CLASS_NAME, "ThingCardBody__cardBodyWrapper--BLLzJ").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "DonwloadButton").click()
time.sleep(15)
driver.back()




driver.quit()