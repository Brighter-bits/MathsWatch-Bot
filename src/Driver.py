from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
option = webdriver.EdgeOptions()
import time
option.add_experimental_option("detach", True)
option.add_argument("start-maximized")#The more space the easier it is to manipulate
option.add_argument("inprivate")#Stops the 'log into edge' window from popping up AND gets rid of the sidebar
# option.add_argument("--headless")
driver = webdriver.Edge(options=option)
actions = ActionChains(driver)
cookies = 0
driver.implicitly_wait(20)
driver.get('https://vle.mathswatch.co.uk')
username = ""
password = ""
if cookies != 0:
    #Note: MathsWatch's cookies are short term, however the login window is absolute hell to navigate through.
    #This does however, bypass the login limit
    #Fix this later
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
else:
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/forminput[1]/formgroup/div/div/span/input')
    actions.click(water).send_keys_to_element(water, username).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/forminput[1]/formgroup/div/div/span/input')
    actions.click(water).send_keys_to_element(water, username).perform()
    #Don't ask why it is done twice. IT JUST WORKS!
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/forminput[2]/formgroup/div/div/span/input')
    actions.click(water).send_keys_to_element(water, password).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/div/div/div/div/button[2]')
    actions.click(water).perform()