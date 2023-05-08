import time
from selenium import webdriver
#You can use this to grab your mathswatch login cookie, they are temporary cookies
driver = webdriver.Edge()
driver.get("https://vle.mathswatch.co.uk/vle")
time.sleep(20)
print(driver.get_cookies())
input("Press enter to close window")
