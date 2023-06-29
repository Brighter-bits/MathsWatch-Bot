from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
option.add_argument("start-maximized")#The more space the easier it is to manipulate
option.add_argument("inprivate")#Stops the 'log into edge' window from popping up AND gets rid of the sidebar
option.add_argument("--disabled-extensions")
option.add_argument("--remote-allow-origins=*")
option.add_experimental_option('excludeSwitches', ['enable-logging'])
# option.add_argument("--headless")
driver = webdriver.Edge(options=option)
actions = ActionChains(driver)
cookies = [{'domain': 'vle.mathswatch.co.uk', 'expiry': 1688058278, 'httpOnly': False, 'name': '_csrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zDLWlTHV-KWKKWcVYUbm20xTtG1ceeNMzWAo'}, {'domain': 'vle.mathswatch.co.uk', 'expiry': 1688054678, 'httpOnly': True, 'name': 'connect.sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 's%3ABGP2SbhCLntFGbYHlw4S5GH-OvNhksMd.8XsGyYQH6B6ke0yNHGXQnKjbknFzC9J7nMlM1HCJsMY'}, {'domain': '.mathswatch.co.uk', 'expiry': 1722611069, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1478145595.1688051069'}, {'domain': '.mathswatch.co.uk', 'expiry': 1722611077, 'httpOnly': False, 'name': '_ga_61P6DK12ZM', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GS1.1.1688051068.1.0.1688051077.0.0.0'}, {'domain': '.mathswatch.co.uk', 'expiry': 1688137469, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.572221477.1688051069'}, {'domain': '.mathswatch.co.uk', 'expiry': 1688051129, 'httpOnly': False, 'name': '_gat_gtag_UA_84289525_1', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}]
driver.implicitly_wait(20)
driver.get('https://vle.mathswatch.co.uk')
try:
    with open("Global Variables.txt", 'r') as f:
        Login = f.readlines() # Open the Global Variables and store the two lines as a single list
        f.close
except:
    pass

if cookies != 0:
    #Note: MathsWatch's cookies are short term, however the login window is absolute hell to navigate through.
    #This does however, bypass the login limit
    #Fix this later
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
else:
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/forminput/formgroup/div/div/span/input')
    actions.click(water).send_keys_to_element(water, Login[0].strip("\n")).perform()
    if Login[2].strip("\n") == "True":
        water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, Login[0].strip("\n")).perform()
    #Don't ask why it is done twice. IT JUST WORKS!
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/div/div/div/div/button[2]/span')
    actions.click(water).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/forminput[2]/formgroup/div/div/span/input')
    actions.click(water).send_keys_to_element(water, Login[1].strip("\n")).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/modal/div[1]/div/div/div[2]/div/div[1]/form/div/div/div/div/button[2]')
    actions.click(water).perform()
    time.sleep(1)