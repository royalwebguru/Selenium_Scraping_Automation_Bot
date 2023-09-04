from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set the proxy details
proxy_host = "geo.iproyal.com"
proxy_port = "12321"
proxy_username = "Dean50GB"
proxy_password = "Dean50GB123_country-fr_session-2ut6f29p_lifetime-24h"

# Create Chrome options
options = Options()

# Set the proxy server
proxy = f"{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
options.add_argument('--proxy-server=http://' + proxy)

# Create a new WebDriver instance with the desired options
driver = webdriver.Chrome(options=options)

# Load the URL using the proxy
driver.get("https://www.metin2pserver.info/vote.htm?id=kime2com&name=196")

while True:
    time.sleep(3)
    print("1")