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
cookies = [{'domain': 'vle.mathswatch.co.uk', 'expiry': 1683846079, 'httpOnly': False, 'name': '_csrf', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'vtQKGzGm-LQhGOPZVy2lI3CmfG2pTqQ3Iqp4'}, {'domain': '.mathswatch.co.uk', 'expiry': 1683838939, 'httpOnly': False, 'name': '_gat', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}, {'domain': '.mathswatch.co.uk', 'expiry': 1683925272, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.2025020349.1683838872'}, {'domain': '.mathswatch.co.uk', 'expiry': 1718398872, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'GA1.3.1560763091.1683838872'}, {'domain': 'vle.mathswatch.co.uk', 'expiry': 1683842479, 'httpOnly': True, 'name': 'connect.sid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 's%3Alm8yHS4SUXlnsGg8dxT-mOjpnvwVgBtZ.ZEaA2lfr0n8GXtTQxry6zLtEaQYG62oEceBalHGb9iI'}]
for cookie in cookies:
    driver.add_cookie(cookie)