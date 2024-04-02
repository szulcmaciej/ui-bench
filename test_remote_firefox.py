# docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.19.0-20240328

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# move mouse
# ActionChains(driver).move_by_offset(13, 15).perform()
# driver.implicitly_wait(1)
# ActionChains(driver).move_by_offset(13, 15).perform()
# driver.implicitly_wait(1)
# ActionChains(driver).move_by_offset(13, 15).perform()
# driver.implicitly_wait(1)
# ActionChains(driver).move_by_offset(13, 15).perform()
driver.close()
