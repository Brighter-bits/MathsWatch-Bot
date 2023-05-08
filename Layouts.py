from Driver import driver
from Driver import actions
from Driver import By
def SymSingleLongBox(answer, next=0):
    """
    This is a function to quickly answer the questions with a single long answer box to the side with an extra small box which has a symbol infront or behind it e.g '£', PM, AM, cm

    answer = the answer to the question

    next = 'L' or 'H' to indicate lower or higher questions followed by the div number (they start at 3). NO SPACES! Leave blank for the final question

    """
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/formgroup/div/div/div/div/div[1]/span[2]')
    actions.send_keys_to_element(water, answer).perform()
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
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div['+str(num2)+']/ul/li['+num+']/a')
        actions.click(water).perform()

def NormSingleLongBox(answer, next=0):
    """
    This is a function to quickly answer the questions with a single long answer box

    answer = the answer to the question

    next = 'L' or 'H' to indicate lower or higher questions followed by the div number (they start at 3). NO SPACES! Leave blank for the final question

    """
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/formgroup/div/div/span/div/div[1]')
    actions.send_keys_to_element(water, answer).perform()
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
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div['+str(num2)+']/ul/li['+num+']/a')
        actions.click(water).perform()
