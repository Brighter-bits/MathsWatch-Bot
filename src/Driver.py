from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
# option.add_argument("--headless")
driver = webdriver.Edge(options=option)
actions = ActionChains(driver)
driver.implicitly_wait(20)
driver.get('https://vle.mathswatch.co.uk')
#Note: MathsWatch's cookies are short term, however the login window is absolute hell to navigate through.
#This does however, bypass the login limit
#Fix this later
driver.delete_all_cookies()
cookies = 
for cookie in cookies:
    driver.add_cookie(cookie)
