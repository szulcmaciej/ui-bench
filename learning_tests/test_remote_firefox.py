# docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.19.0-20240328
# for debugging or viewing open http://localhost:7900/?autoconnect=1&resize=scale&password=secret
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)
try:
   driver.get("https://www.windguru.cz/station/3428")
   assert "Matas Blancas" in driver.title
   driver.implicitly_wait(5)
   import time
   time.sleep(1)
   elem = driver.find_element(By.CLASS_NAME, "wgs_wind_avg_value")
   driver.save_screenshot('prtscrn.png')
   wind_speed = elem.text
   print(f'{wind_speed=}')
   assert "No results found." not in driver.page_source

finally:
   driver.quit()
   