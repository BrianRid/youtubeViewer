from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time
import os

for i in range(2):
  chromedriver = './chromedriver'
  os.environ['webdriver.chrome.driver'] = chromedriver
  driver = webdriver.Chrome(chromedriver)
  driver.get('https://consent.youtube.com/m?continue=https://www.youtube.com/watch%3Fv%3D6vUmA09EKMQ%26t%3D2246%26themeRefresh%3D1%26cbrd%3D1&gl=FR&m=0&pc=yt&hl=fr&src=1')
  time.sleep(25)
  no_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Tout refuser')]")

  ActionChains(driver).move_to_element(no_button).click(no_button).perform()

  time.sleep(25)
  driver.close()
