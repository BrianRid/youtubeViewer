from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time
import os

url = input('Enter the youtube url : ')
views = int(input('Enter the number of views you want to add : '))


for i in range(views):
  chromedriver = './chromedriver'
  os.environ['webdriver.chrome.driver'] = chromedriver
  driver = webdriver.Chrome(chromedriver)
  driver.get(url)
  time.sleep(25)
  no_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Tout refuser')]")

  ActionChains(driver).move_to_element(no_button).click(no_button).perform()

  time.sleep(120)
  driver.close()
