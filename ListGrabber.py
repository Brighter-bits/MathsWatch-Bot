#A list which takes the module ID and puts them in a dictionary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
option.add_argument("start-maximized")#The more space the easier it is to manipulate
option.add_argument("inprivate")#Stops the 'log into edge' window from popping up AND gets rid of the sidebar
option.add_argument("--headless")
driver = webdriver.Edge(options=option)
actions = ActionChains(driver)
cookies = [{'domain': 'vle.mathswatch.co.uk', 'expiry': 1686835908, 'httpOnly': False, 'name': '_csrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '4LjBfkIL-S8oYCH2RrYAbZQQpMtOuQrih1fw'}, {'domain': 'vle.mathswatch.co.uk', 'expiry': 1686832308, 'httpOnly': True, 'name': 'connect.sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 's%3AG_ec85MzXI4Dbfy350KABmEdRUlZCiA1.2OmiTQuS14gDvGtkaXiiTC6w%2BQEgDR54M2gnjbR8x8E'}, {'domain': '.mathswatch.co.uk', 'expiry': 1721388698, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1988015251.1686828699'}, {'domain': '.mathswatch.co.uk', 'expiry': 1721388707, 'httpOnly': False, 'name': '_ga_61P6DK12ZM', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GS1.1.1686828698.1.0.1686828707.0.0.0'}, {'domain': '.mathswatch.co.uk', 'expiry': 1686915098, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.422247700.1686828699'}, {'domain': '.mathswatch.co.uk', 'expiry': 1686828758, 'httpOnly': False, 'name': '_gat_gtag_UA_84289525_1', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}]   
driver.implicitly_wait(20)
driver.get('https://vle.mathswatch.co.uk')
SmallPP = {}

driver.delete_all_cookies()
for cookie in cookies:
    driver.add_cookie(cookie)

for i in range(126):
    driver.get('https://vle.mathswatch.co.uk/vle/stats/')
    water = Select(driver.find_element(by=By.XPATH, value = '/html/body/app/main/div[2]/routehandler/div/panel/div/student-stats/div[2]/div[2]/div/div[1]/div[2]/select'))
    water.select_by_visible_text('Primary')
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/panel/div/student-stats/div[2]/div[2]/div/div[2]/table/tbody/tr[' + str(i+1) + ']/td[3]/a')
    actions.move_to_element(water).click().perform()
    SmallPP[i+1] = int(driver.current_url.replace("https://vle.mathswatch.co.uk/vle/browse/", ""))

with open('SmallPP.txt', 'w') as f:
    f.write(str(SmallPP))
    f.close

print("Dictionaries and Thesauruses Successfully stolen")
