import capsolver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("userAgent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58")

driver = webdriver.Chrome(options=options)

driver.get("https://www.metin2pserver.info/vote.htm?id=Narco2&name=191")

CAPSOLVER_API_KEY="CAI-CA8F5D78B888FEB049BE5444950CAA9F"

capsolver.api_key = CAPSOLVER_API_KEY

balance = capsolver.balance()
print(balance)

# driver.execute_script("document.querySelector('input[value=\"Vote!\"]').click()")

solution = capsolver.solve({
            "type": "ReCaptchaV2TaskProxyLess",
            "websiteURL": "https://www.metin2pserver.info/vote.htm?id=Narco2&name=191",
            "websiteKey": "6Le9IgUTAAAAAP0DeUdMBBlguRTvEwZtDHA18tQ8"
          })

# driver.find_element(By.ID, "recaptcha-demo-submit").click()
# driver.execute_script("document.querySelector('input[value=\"Vote!\"]').click()")

print(solution)
# time.sleep(10)

# solution1 = capsolver.solve({
#     "type": "AntiCloudflareTask",
#     "websiteURL": "https://cfschl.peet.ws/",
#     "proxy": "socks5:iproyal.com:12321:Dean50GB:Dean50GB123_country-fr_session-2ut6f29p_lifetime-24h"
# })
# print(solution1)
# driver.execute_script("document.querySelector('input[type=\"checkbox\"]').click()")
# driver.execute_script('document.getElementsByClassName("ctp-label")[0].click()')

while True:
    time.sleep(3)
    print("1")