from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://wordpress.com")

refreshrate = int(3)

while True:
    time.sleep(refreshrate)
    driver.refresh()