from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome Browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find search box
search_box = driver.find_element(By.NAME, "q")

# Type search query
search_box.send_keys("Python Programming")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait for results
time.sleep(5)

print("Search completed successfully!")

# Close browser
driver.quit()