import capsolver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.FirefoxOptions()
options.add_argument("--headless")
options.add_argument("userAgent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58")

driver = webdriver.Firefox(options=options)

driver.get("https://www.metin2pserver.info/vote.htm?id=kime2com&name=29779")

CAPSOLVER_API_KEY="CAI-CA8F5D78B888FEB049BE5444950CAA9F"

capsolver.api_key = CAPSOLVER_API_KEY

balance = capsolver.balance()
print(balance)

print(driver.current_url)

token = ''

try:
    driver.execute_script("document.querySelector('input[value=\"Vote!\"]').click()")
    time.sleep(5)
    print(driver.current_url)

    sss = driver.find_element(By.ID, "challenge-running")
    _value = sss.get_attribute('class')
    print(str(_value))

    solution1 = capsolver.solve({
        "type": "AntiCloudflareTask",
        "websiteURL": "https://www.metin2pserver.info/vote-kime2com.htm",
        "proxy": "http:geo.iproyal.com:12321:Dean50GB:Dean50GB123_country-fr_session-67h3gr6g_lifetime-24h"
    })
    print("cloudflare response: ")
    print(solution1['token'])
    token = solution1['token']
except:
    print("can't find element")

# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)

time.sleep(5)
print(driver.current_url)

# _cookie = {
#     "name": "cf_clearance",
#     "value": token,
#     "httpOnly": True,
#     "secure": True
# }

# driver.add_cookie(_cookie)

# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)

# driver.refresh()

# driver.get("https://www.metin2pserver.info/vote-Narco2.htm")

# driver.execute_script("document.cookie='__cf_chl_tk=" + token + "; path=/; domain=.example.com';")
time.sleep(4)
print(driver.current_url)


# driver.execute_script("document.querySelector('input[value=\"Vote!\"]').click()")

# qqq = driver.find_element(By.CSS_SELECTOR, "input[title='Vote 4 kime2com!']")
# _value_qqq = qqq.get_attribute('type')
# print(str(_value_qqq))

solution = capsolver.solve({
    "type": "ReCaptchaV2TaskProxyLess",
    "websiteURL": "https://www.metin2pserver.info/vote.htm?id=Narco2&name=191",
    "websiteKey": "6Le9IgUTAAAAAP0DeUdMBBlguRTvEwZtDHA18tQ8"
})

# # driver.find_element(By.ID, "recaptcha-demo-submit").click()
# # driver.execute_script("document.querySelector('input[value=\"Vote!\"]').click()")
print("captcha response: ")
print(solution['gRecaptchaResponse'])
# time.sleep(4)
print('\n')

print(solution)



# solution1 = capsolver.solve({
#     "type": "AntiCloudflareTask",
#     "websiteURL": "https://cfschl.peet.ws/",
#     "proxy": "socks5:geo.iproyal.com:12321:Dean50GB:Dean50GB123_country-fr_session-2ut6f29p_lifetime-24h"
# })
# print(solution1)
# # driver.execute_script("document.querySelector('input[type=\"checkbox\"]').click()")
# # driver.execute_script('document.getElementsByClassName("ctp-label")[0].click()')

while True:
    time.sleep(3)
    print("1")