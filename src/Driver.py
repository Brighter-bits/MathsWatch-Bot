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
cookies = [{'domain': 'vle.mathswatch.co.uk', 'expiry': 1683926518, 'httpOnly': False, 'name': '_csrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'HQDH8QyW-pvCrFl_PaLSZTMf8kM7wRnvxa-Q'}, {'domain': '.mathswatch.co.uk', 'expiry': 1683919377, 'httpOnly': False, 'name': '_gat', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': '.mathswatch.co.uk', 'expiry': 1684005704, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.899466937.1683919304'}, {'domain': '.mathswatch.co.uk', 'expiry': 1718479304, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1804019397.1683919304'}, {'domain': 'vle.mathswatch.co.uk', 'expiry': 1683922918, 'httpOnly': True, 'name': 'connect.sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 's%3AA4jSTWGtd80RmupaO110gaCm5sYdOvKb.p%2FEDCQId8YxJHcJINJv2idcL44lJWdOeL835mHUWThI'}]
for cookie in cookies:
    driver.add_cookie(cookie)