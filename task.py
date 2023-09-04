from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.metin2pserver.info/vote.htm?id=kime2com&name=196")

refreshrate = int(20)

while True:
    time.sleep(refreshrate)
    driver.refresh()