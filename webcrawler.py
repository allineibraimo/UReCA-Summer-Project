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

time.sleep(4)

driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
time.sleep(2)

stls = driver.find_elements(By.CLASS_NAME, "ThingCard__thingCard--fG91n")

time.sleep(4)

for link in stls:
    WebDriverWait(driver, 3).until(EC.invisibility_of_element_located(link))
    link.click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@class= "Button__button--xv8c4 Button__primary--grPsm Button__left--Zsp9y Button__md--hfp1W Button__icon--UCU2X"]').click()
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, "Modal__closeButton--GTlJu").click()
    time.sleep(4)
    driver.back()
    time.sleep(3)
    driver.refresh()
    time.sleep(8)

# driver.find_element(By.CLASS_NAME, "ThingCardBody__cardBodyWrapper--BLLzJ").click()
# time.sleep(6)
# driver.find_element(By.XPATH, '//button[@class= "Button__button--xv8c4 Button__primary--grPsm Button__left--Zsp9y Button__md--hfp1W Button__icon--UCU2X"]').click()
# time.sleep(10)
# driver.find_element(By.CLASS_NAME, "Modal__closeButton--GTlJu").click()
# time.sleep(3)
# driver.back()
# time.sleep(4)


# <button class="Button__button--xv8c4 Button__primary--grPsm Button__left--Zsp9y Button__md--hfp1W Button__icon--UCU2X"><img class="" src="https://cdn.thingiverse.com/site/assets/inline-icons/1f6b7330c1fc454b22fe.svg" alt="DownloadButton" loading="lazy">Download All Files</button>

driver.quit()