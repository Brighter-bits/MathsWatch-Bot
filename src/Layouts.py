from Driver import driver
from Driver import actions
from Driver import By
recurrence=1
def SymLongBox(answer, next=0, second="Melons", third="Melons", fourth="Melons"):
    """
    This is a function to quickly answer the questions with a single long answer box to the side with an extra small box which has a symbol infront or behind it e.g '£', PM, AM, cm

    answer = the answer to the question

    second = the answer to the second box, so on for third and fourth

    next = 'L' or 'H' to indicate lower or higher questions followed by the question number. NO SPACES! Leave blank for the final question

    """
    if second == "Melons":
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/formgroup/div/div/div/div/div[1]/span[2]')
        actions.send_keys_to_element(water, answer).perform()
    else:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]/span[2]')
        actions.send_keys_to_element(water, answer).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]/span[2]')
        actions.send_keys_to_element(water, second).perform()
        if third != "Melons":
            water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]/span[2]')
            actions.send_keys_to_element(water, third).perform()
            if fourth != "Melons":
                water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/div/div/div[1]/span[2]')
                actions.send_keys_to_element(water, fourth).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
    actions.click(water).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
    actions.click(water).perform()
    if next != 0:
        level = next.rstrip("1234567890")
        num = next.lstrip("LHlh")
        if level == "H" or level == "h":
            num2 = 3
        else:
            num2 = 1
        for bob in range(recurrence):
            driver.implicitly_wait(20)
            water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div['+str(num2)+']/ul/li['+str(int(num)+2)+']/a')
            actions.click(water).perform()
            #Does this twice to allow for smaller screens to click on the next arrow and the next questions /// Bugged 

def NormLongBox(answer, next=0, second="Tangerine", third="Tangerine", fourth="Tangerine", fifth="Tangerine"):
    """
    This is a function to quickly answer the questions with a single long answer box

    answer = the answer to the question

    second = the answer to the second box, so on for third and fourth

    next = 'L' or 'H' to indicate lower or higher questions followed by the question number. NO SPACES! Leave blank for the final question

    """
    if second == "Tangerine":
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, answer).perform()
    else:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, answer).perform()
        if second != 0:#A few questions use this xpath for some reason (possibly due to the extra symbols button in the box), so if second = 0 then that means to use the different XPath but there is NOT a second box
            water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
            actions.send_keys_to_element(water, second).perform()
            if third != "Tangerine":
                water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
                actions.send_keys_to_element(water, third).perform()
                if fourth != "Tangerine":
                    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
                    actions.send_keys_to_element(water, fourth).perform()
                    if fifth != "Tangerine":
                        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[5]/div/subtag/div/formgroup/div/div/span/div/div[1]')
                        actions.send_keys_to_element(water, fifth).perform()

    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
    actions.click(water).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
    actions.click(water).perform()
    if next != 0:
        level = next.rstrip("1234567890")
        num = next.lstrip("LHlh")
        if level == "H" or level == "h":
            num2 = 3
        else:
            num2 = 1
        for bob in range(recurrence):
            driver.implicitly_wait(20)
            water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div['+str(num2)+']/ul/li['+str(int(num)+2)+']/a')
            actions.click(water).perform()

def divinput2(first = "kumquats", next = 0, second = "kumquats", third = "kumquats", fourth = "kumquats", fifth = "kumquats"):
    """
    This is a function to quickly answer questions in the white area (directly next to the question)
    
    next = 'L' or 'H' to indicate lower or higher questions followed by the question number. NO SPACES! Leave blank for the final question

    first = the answer to the first question. So on, so forth for second, third and fourth

    Note: This might be more inefficient but it will be easier to read and maintain
    """
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
    actions.send_keys_to_element(water, first).perform()
    if second != "kumquats":
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, second).perform()
        if third != "kumquats":
            water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
            actions.send_keys_to_element(water, third).perform()
            if fourth != "kumquats":
                water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
                actions.send_keys_to_element(water, fourth).perform()
                if fifth != "kumquats":
                    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[6]/div/input')
                    actions.send_keys_to_element(water, fifth).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
    actions.click(water).perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
    actions.click(water).perform()
    if next != 0:
        level = next.rstrip("1234567890")
        num = next.lstrip("LHlh")
        if level == "H" or level == "h":
            num2 = 3
        else:
            num2 = 1
        for bob in range(recurrence):
            driver.implicitly_wait(20)
            water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div['+str(num2)+']/ul/li['+str(int(num)+2)+']/a')
            actions.click(water).perform()