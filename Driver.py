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
cookies = [{'domain': 'vle.mathswatch.co.uk', 'expiry': 1683572853, 'httpOnly': False, 'name': '_csrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'jhx1TYQJ-r2oq5tXdfM6LxSj0_5hu9YmCP1Y'}, {'domain': '.mathswatch.co.uk', 'expiry': 1683565712, 'httpOnly': False, 'name': '_gat', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': '.mathswatch.co.uk', 'expiry': 1683652041, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1290039038.1683565641'}, {'domain': '.mathswatch.co.uk', 'expiry': 1718125641, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1334723512.1683565641'}, {'domain': 'vle.mathswatch.co.uk', 'expiry': 1683569253, 'httpOnly': True, 'name': 'connect.sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 's%3Aiz1uyIWJq5_z3rSYIXUk9e3P3POvedKL.wm8%2FFK5rnx3z5ptRKfbRFOyx940ZxA%2B199tiUZdMwNY'}]
for cookie in cookies:
    driver.add_cookie(cookie)