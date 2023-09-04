from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Find the search input element and enter a query
search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Python Selenium")

# Submit the search form
search_input.submit()

driver.implicitly_wait(10)

# Find all the search result titles and print them
search_results = driver.find_elements(By.CSS_SELECTOR, "h3")
for result in search_results:
    print(result.text)

# Close the browser
driver.quit()