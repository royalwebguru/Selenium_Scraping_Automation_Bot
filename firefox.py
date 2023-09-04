import capsolver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.metin2pserver.info/vote.htm?id=Narco2&name=191")


CAPSOLVER_API_KEY="CAI-CA8F5D78B888FEB049BE5444950CAA9F"

capsolver.api_key = CAPSOLVER_API_KEY

balance = capsolver.balance()
print(balance)



# _s = driver.find_element(By.NAME, 's')
# _id = driver.find_element(By.NAME, 'id')
# _param_user = driver.find_element(By.NAME, 'param_user')

# _s_value = _s.get_attribute('value')
# _id_value = _id.get_attribute('value')
# _param_user_value = _param_user.get_attribute('value')
# print("s: " + str(_s_value) + "\n" + "id: " + str(_id_value) + "\n" + "param_user: " + str(_param_user_value))


# x_coordinate = 873
# y_coordinate = 329

# actions = ActionChains(driver)

# time.sleep(3)
# actions.move_by_offset(x_coordinate, y_coordinate).click().perform()






solution = capsolver.solve({
    "type": "AntiCloudflareTask",
    "websiteURL": "https://www.metin2pserver.info/vote-kime2com.htm",
    "proxy": "socks5:geo.iproyal.com:12321:Dean50GB:Dean50GB123_country-fr_session-2ut6f29p_lifetime-24h"
})
print(solution)

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