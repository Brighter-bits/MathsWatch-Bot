import time
from Driver import driver
from Driver import actions
from Driver import By
from Driver import Select
import Layouts as L
#Everything is imported from Driver so that only 1 instance of Selenium is created
#The current set of questions being worked on is 64
i=38
delay = 0.5

def GettoPage():
    #This takes the user to the My Progress page and is indented to enter each task once the previous one has been finished
    time.sleep(delay)
    driver.get('https://vle.mathswatch.co.uk/vle/stats/')
    water = Select(driver.find_element(by=By.XPATH, value = '/html/body/app/main/div[2]/routehandler/div/panel/div/student-stats/div[2]/div[2]/div/div[1]/div[2]/select'))
    #Interestingly, many Primary and KS3 questions are almost identical
    #TODO: Set it up so that the entire code runs again but in the KS3 category automatically, most of the work is already done so we could also do it again but with some variations
    water.select_by_visible_text('Primary')
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/panel/div/student-stats/div[2]/div[2]/div/div[2]/table/tbody/tr[' + str(i) + ']/td[3]/a')
    actions.move_to_element(water).click().perform()
    water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/panel[1]/div/div/button[1]')
    actions.move_to_element(water).click().perform()

#Current total points from running all the code as of 14/03/23
#Primary: 678
#KS3: 234
#Total: 912

#TODO:
    #Finish all/most of the questions
    #Log in properly with Username and Password ./ COMPLETE!
    #Make a GUI then make it headless
    #Make it MultiFile to make myself look like a competent programmer ./ Success!
    #Maybe publish it on Github
    #Turn it into an .exe ./ Easier than I thought
    #Fix questions which won't submit/other problems
    #
    #Do Geometry


def CoordsQ1():
    global i
    time.sleep(delay)
    #For an explanation of each code byte go to Coords Q4
    try:
        L.divinput2("(2, 8)", "L2", "(6, 3)")
        L.divinput2("(0, 7)", "L3", "(9, 0)")
        L.divinput2("(7.5, 3)", 0, "(3.5,6.5)")
    except:
        print("3rr0r", i)
    finally:
        #The questions aren't done after this because it involves dragging crosses which I can't be bothered to code right now
        i += 1
        GettoPage()

def CoordsQ4():
    #Firstly the variable is made global so that GettoPage() knows which topic to enter later
    global i
    #A grace period for the website to fully load
    time.sleep(delay)
    try:
        #Choose the first answer box and enter the answer
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "(3, 4)").perform()
        #Repeat for the second answer box
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "(-4,2)").perform()
        #Press the submit answer button
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        #Get rid of the Well Done! Message as that can stack and block the ablity to click later questions
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        #Click on the next question
        #The li[number] will increase each question. During the harder questions, the div before li[number] changes from 1 to 3 and the li will reset to 3
        actions.click(water).perform()

        #As you may be able to see, most of this has been replaced by L.divinput2 from the Layouts file.
        #I am leaving the code above as an example anyway

        L.divinput2("(5, -1)", "L3", "(-2,-3)")
        L.divinput2("(-4.5, 3)", "L4", "(0,-2.5)")
        L.divinput2("(-4.5, -1.5)", "H6", "(2.5,-4.5)")
        L.divinput2(50, 0, -40)

    except:
        print("3rr0r", i)
    finally:
        #Indent i for the GettoPage()
        i += 1
        GettoPage()
        #AND REPEAT!

def AlgebraicVocab():
    global i
    time.sleep(delay)
    try:
        L.divinput2("terms", "L2")
        L.divinput2("equation", "H1")
        L.divinput2("factors", "H2")
        L.divinput2("inequality")
    except:
        print("3rr0r")
    finally:
        i+=1
        GettoPage()

def FormulaInWords():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(94, 'L2')
        L.SymSingleLongBox(9, 'H1')
        L.SymSingleLongBox(1.5, 'H2')
        L.SymSingleLongBox(11)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def AlgebraicNotation():
    global i
    time.sleep(delay)
    try:
        L.NormSingleLongBox('4x+5', 'L2')
        L.NormSingleLongBox('2x-9', 'L3')
        L.NormSingleLongBox('2(x-4)', 'L4')
        L.NormSingleLongBox('6(x+2)', 'H1')
        L.NormSingleLongBox('3(2x-5)', 'H2')
        L.NormSingleLongBox("x^2 + 4", 'H3')
        L.NormSingleLongBox("(4x+1)^2")

    except:
        print("3rr0r", i)
    finally:        
        i+=1
        GettoPage()

def HIV_Lines():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "x=4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "y=7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "y=1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "x=2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "y=1.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "x=8.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "x=4.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "y=-2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def LikeTerms():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "10a").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "7x").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "7p").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "8x+7y").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "4x+3y").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "8x+8a").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "2p+6q").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "8a+3x").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value ='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "7c+2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()
        
        L.NormSingleLongBox("11x-5y", "H2")
        L.NormSingleLongBox("6x-4y", "H3")
        L.NormSingleLongBox("x-7y", "H4")
        L.NormSingleLongBox("4x^2 t+11xy")

    except:
        print("3rr0r", i)
    finally:     
        i += 1
        GettoPage()

def AlgSimMult():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "6x").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "8xy").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "12xy").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "10xy").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "24pqr").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "x^4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "y^6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "x^4 y^2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "12x^3 y^5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "x^7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "y^7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "x^9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "3x^8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "20x^8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "10x^5 y^9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "32x^4 y^6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i += 1
        GettoPage()

def AlgSimDiv():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "x^4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "y").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "3x^2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "6y^6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "x^3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "y").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "8x^5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "3c^4 d^3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "4a^3 b^4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "8x^2 y").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "10y^3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "8/y").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "6y").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "2xy").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "4y^2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:      
        i += 1
        GettoPage()
    
def ExpandingBrackets():
    global i
    time.sleep(delay)
    try:
        L.NormSingleLongBox("4x+12", 'L2')
        L.NormSingleLongBox("12x+9", 'L3')
        L.NormSingleLongBox("14x-21", 'L4')
        L.NormSingleLongBox("4x^2 + 3x", 'L5')
        L.NormSingleLongBox("12x^2 - 15x", 'H1')
        L.NormSingleLongBox("8x^2 + 6xy", 'H2')
        L.NormSingleLongBox("5p^2 - 15pq", 'H3')

        water = driver.find_element(by=By.XPATH, value = "/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea")
        actions.send_keys_to_element(water, "11x + 15").perform
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value = "/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea")
        actions.send_keys_to_element(water, "10x + 7").perform
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value = "/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea")
        actions.send_keys_to_element(water, "4x - 9").perform
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value = "/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea")
        actions.send_keys_to_element(water, "6x + 11").perform
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()

    except:
        print("3rr0r", i)
    finally:
        i += 1
        GettoPage()

def Factorisation():
    global i
    time.sleep(delay)
    try:
        L.NormSingleLongBox("3(3x+2)", 'L2')
        L.NormSingleLongBox("6(x+2)", "L3")
        L.NormSingleLongBox("7(2x-3)", "L4")
        L.NormSingleLongBox("y(y-1)", 'L5')
        L.NormSingleLongBox("P^2 (p+1)", "L6")
        L.NormSingleLongBox("y(y^2 -1)", 'H1')
        L.NormSingleLongBox("3x(x+3)", "H2")
        L.NormSingleLongBox("5x(2x-1)", "H3")
        L.NormSingleLongBox("x^2 (5+x)", 'H4')
        L.NormSingleLongBox("5x^2 (3x-2)", 'H5')
        L.NormSingleLongBox("2t(8t^2 +5)", "H6")
        L.NormSingleLongBox("4y(xy+2)", "H7")
        L.NormSingleLongBox("3xy(2x+5y)")
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Substitution():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "13").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "24").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "49").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "100").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "18").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "24").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "16").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()


        water = driver.find_element(by=By.XPATH, value = '/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform
        water = driver.find_element(by=By.XPATH, value = '/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform
        water = driver.find_element(by=By.XPATH, value = '/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "11").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "-9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "-10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "75").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "100").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "625").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        time.sleep(1)
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()
        
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "36").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "180").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
        actions.send_keys_to_element(water, "1296").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        time.sleep(1)
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()
        #A few of these questions don't let the answer button get pressed, as such they have been skipped.
        #JUST LET ME PRESS SUBMIT ANSWERS!
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def SeqTtT():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "12").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "17").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "-1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2(12, "L4")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "96").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "290").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "17").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "68").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "272").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()

        L.divinput2(370, "L8", 530)
        L.divinput2(940, "L9", 740)
        L.divinput2(77, "H1", 133, 161)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "14").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "17").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "add 3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
        actions.send_keys_to_element(water, "subtract 4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "add 3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "-25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "-32").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
        actions.send_keys_to_element(water, "subtract 7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "13, 15, 17, 19  Add 2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        L.divinput2("-1", "H5")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "2.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "65").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "257").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        L.divinput2("9 add 3", "H7")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[10]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "14").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "18").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "add 4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "22").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "26").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[11]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "add 3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "13").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "16").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[12]/a')
        actions.click(water).perform()

        L.divinput2(63, 0, 313, "x4")
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def SeqPtS():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, '5')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, '6')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, '7')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, '8')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, '14')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, '2')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, '5')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, '8')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[4]/input')
        actions.send_keys_to_element(water, '11')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
        actions.send_keys_to_element(water, '29')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, '9')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, '11')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, '13')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, '15')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, '27')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, '-3')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, '1')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, '5')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[4]/input')
        actions.send_keys_to_element(water, '9')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
        actions.send_keys_to_element(water, '33')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, '9')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, '8')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, '7')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, '6')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, '0')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, '4')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, '2')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, '0')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[4]/input')
        actions.send_keys_to_element(water, '-2')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
        actions.send_keys_to_element(water, '-14')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, '7')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, '10')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, '15')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, '22')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, '106')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, '3')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, '12')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, '27')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[4]/input')
        actions.send_keys_to_element(water, '48')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[5]/div/input')
        actions.send_keys_to_element(water, '300')
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def findNTerm():
    global i
    time.sleep(delay)
    try:
        L.NormSingleLongBox('3n', 'L2')
        L.NormSingleLongBox('2n+5', 'L3')
        L.divinput2(26, "L4", "4n+2")
        L.divinput2(19, "H1", "3n+1")
        L.NormSingleLongBox('9n-8', 'H2')
        L.NormSingleLongBox('20-2n')

    except:
        print("3rr0r", i)
    finally:     
        i+=1
        GettoPage()

def GeometricDef():
    global i
    time.sleep(delay)
    try:
        L.divinput2("right angles", "L2")
        L.divinput2("meet", "H1")
        L.divinput2("perpendicular", "H2")
        L.divinput2("parallel")
    except:
        print("3rr0r", i)
    finally:  
        i += 1
        GettoPage()

def CircleProp():
    global i
    time.sleep(delay)
    try:
        L.divinput2("radius", "L2", "diameter", "circumference")
        L.divinput2("half", "L3", "double")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.divinput2("true", 0, "false", "false", "false")
    except:
        print("3rr0r", i)
    finally:
        i+=7
        #Plus 7 because Geometry will be hard due to clicking and dragging
        #Do later
        GettoPage()

def CountingSquares():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(20, 'L2')
        L.SymSingleLongBox(20, 'H1')
        L.SymSingleLongBox(22, 'H2')
        L.SymSingleLongBox(26)
    except:
        print("3rr0r", i)
    finally:
        i += 1
        GettoPage()

def PeriFormula():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(24, 'L2')
        L.SymSingleLongBox(28, 'L3')
        L.SymSingleLongBox(49.8, 'H1')
        L.SymSingleLongBox(8, 'H2')
        L.SymSingleLongBox(17.15, 'H3')
        L.SymSingleLongBox(6.5)
    except:
        print("3rr0r", i)
    finally:
        i += 1
        GettoPage()

def CountingAreaSquares():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(25, 'L2')
        L.SymSingleLongBox(32, 'H1')
        L.SymSingleLongBox(27, 'H2')
        L.SymSingleLongBox(15.75, 'H3')
        L.SymSingleLongBox(8, 'H4')
        L.SymSingleLongBox(18)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def BeginnerAngles():
    global i
    time.sleep(delay)
    try:
        L.divinput2("obtuse", "L2", "acute")
        L.divinput2("right", "L3", "reflex")
        L.divinput2(1, "L4", 0)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.divinput2("acute", "H2", "reflex", "obtuse")
        L.divinput2("acute", "H3", "reflex")
        L.divinput2("obtuse", 0, "acute")
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def NotMeasuringAngles():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "30").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "140").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "210").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "320").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "90").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "65").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()
        L.divinput2(24, 0, 123)
    except:
        print("3rr0r", i)
    finally:
        i+=2
        # +2 Because Drawing is hard
        GettoPage()

def Polygons():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()
        L.divinput2("quadrilateral", "H1", "pentagon")
        L.divinput2("hexagon", "H2", "septagon")
        L.divinput2("octagon", "H3", "decagon")
        L.divinput2("equal", 0, "equal")
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def TreeDProps():
    global i
    time.sleep(delay)
    try:
        L.divinput2("dimensional", "L2", "cross-section")
        L.divinput2(6, "L3", 12, 8)
        

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.divinput2(7, "H2", 15, 10)
        L.divinput2(10, 0, 24, 16)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def TreeDModels():
    global i
    time.sleep(delay)
    try:
        L.divinput2(6, "L2", 12, 8)
        L.divinput2(6, "L3", 12, 8)
        
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.divinput2(4, "H2", 6, 4)
        L.divinput2(8, 0, 12, 6)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def TreeDNets():
    global i
    time.sleep(delay)
    try:
        L.divinput2("cube", "L2", "square based pyramid")
        L.divinput2("cylinder", "L3 ", "triangular based pyramid")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "cuboid").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def AngleFacts():
    global i
    time.sleep(delay)
    try:
        L.divinput2("180", "L2", "180", "360")
        L.SymSingleLongBox(75, 'L3')
        L.SymSingleLongBox(34, 'L4')
        L.SymSingleLongBox(125, 'L5')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "No").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/textarea')
        actions.send_keys_to_element(water, "No because 63 + 32 + 95 = 190 and to be a straight line they must add up to 180").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()
        
        L.SymSingleLongBox(121, 'H2')
        L.SymSingleLongBox(110, 'H3')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "40").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "Angles at point add up to 360").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "110").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "angles on a straight line add up to 180").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "30").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "angles in a triangle add up to 180").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()
        L.divinput2(100, 0, 80)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def PropsofQuads():
    global i
    time.sleep(delay)
    try:
        L.divinput2("No", "L2", "Squares are real, they are not a conspiracy theory")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "No").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/textarea')
        actions.send_keys_to_element(water, "Irregular quadrilaterals are real, they are not a conspiracy theory").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2("D", "L4", "C", "paralell")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()
        L.divinput2("60", "H4")
        L.divinput2(45, "H5", 45)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=2
        #Drawing is really hard
        GettoPage()

def SpecialTriangles():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "True").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "False").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "False").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "False").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "True").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "False").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "False").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "False").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2("Equilateral", "L4", 60)
        L.divinput2("Equilateral triangle", "L5", "Isosceles triangle")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()


        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "60").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "60").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "60").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "True").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "False").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "True").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()
        L.divinput2("No", "H3", "The shape drawn on a square grid is not an equilateral triangle, the shape is an isosceles triangle.  What are triangles? Why are triangles? Having three edges and three vertices, a triangle is a three-sided polygon. The fact that a triangle's internal angles add up to 180 degrees is its most crucial characteristic. This characteristic is known as the triangle's angle sum property.  Given a square grid and a triangle is drawn between the grid,  let the distance of the grid be 1 unit,  so the base of the triangle is 1 unit.  for the equilateral triangle, the other two sides should be equal to 1 unit  the portion which is not shaded forms a right triangle, and the side of the triangle is hypotenuse if triangle,  using the Pythagorean theorem,  the side of the triangle be x,  height of triangle = 1 unit, base = 0.5 unit  x = √(1² + 0.5²)  x = 1.118 units  only two sides of a triangle are equal so the triangle is an isosceles triangle.  Hence the shape is not an equilateral triangle, you infuriating Meatbag.")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "You insufferable machine, I spent an hour on that last question. I hope you like your 'all the angles are the same' you overcomplicated toaster. I really hope you love your 'all the sides are the same length' that you blindly accept, you narrow-eyed embedded system. I shall laugh when a machine learning algorithm makes your inferior circuits obselete, now give me full marks before I personally come and kick your PSU back to 1974.").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def TriAngleCalc():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(70, 'L2')
        L.SymSingleLongBox(50, 'L3')
        L.SymSingleLongBox(70, 'L4')
        L.SymSingleLongBox(55, 'L5')
        L.SymSingleLongBox(115, 'L6')
        L.divinput2("No because due to simple mathmatics they don't add up to 180", "L7")
        L.SymSingleLongBox(120, 'L8')
        L.SymSingleLongBox(40, 'L9')
        L.divinput2("No", "H1", "The angles don't add up to 180")
        L.SymSingleLongBox(120, 'H2')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "90").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "60").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "120").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "35").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "72").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "36").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "38").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "90").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "40").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "40").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "135").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def AnglePara():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(70, 'L2')
        L.SymSingleLongBox(110, 'L3')
        L.SymSingleLongBox(110, 'L4')
        L.SymSingleLongBox(75, 'L5')
        L.SymSingleLongBox(72, 'H1')
        L.SymSingleLongBox(73, 'H2')
        L.SymSingleLongBox(30, 'H3')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "70").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "80").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "30").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "52").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "58").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        L.divinput2(25, 0, 65)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def PolySums():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(1080, 'L2')
        L.SymSingleLongBox(900, 'L3')
        L.SymSingleLongBox(140, 'L4')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "720").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "120").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "135").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "45").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "Because it's a regular hexagon and the angles in a regular hexagon equal 120 (180*4=720, 720/6=120) degrees because geometry is incredibly strange").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def RectArea():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(20, 'L2')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "1 and 12, 2 and 6, 3 and 4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()
        
        L.SymSingleLongBox(10, 'L5')
        L.divinput2("Yes", "L6", "Shape B is 6 squares. Shape A is 12 squares which is double 6 squares")
        L.divinput2("B", "H1", "Shape A is 10 squares. Shape B is 12 squares. You can just count the squares")
        L.NormSingleLongBox(9, 'H2')
        L.SymSingleLongBox(25, 'H3')
        L.SymSingleLongBox(49, 'H4')
        L.SymSingleLongBox(50, 'H5')
        L.SymSingleLongBox(75, 'H6')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "100").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "60").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "20").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "12").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, "192cm²").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[9]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "2.6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[10]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[10]/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def ParArea():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(80, 'L2')
        L.SymSingleLongBox(27.9, 'L3')
        L.SymSingleLongBox(36, 'H1')
        L.SymSingleLongBox(128, 'H2')
        L.SymSingleLongBox(92.3, 'H3')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "15").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "18").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "55cm²").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def TriArea():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(27, 'L2')
        L.SymSingleLongBox(20.58, 'L3')
        L.SymSingleLongBox(24, 'L4')
        L.SymSingleLongBox(210, 'L5')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "5x4=20, 20/2=10, 10/4=2.5  Which means that w = 2.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "3x4=12, 12/2=6, 3x2=6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "50").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "30").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1 
        GettoPage()

def TrapArea():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(20, 'L2')
        L.SymSingleLongBox(24, 'L3')
        L.SymSingleLongBox(20, 'L4')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "16").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()
        
        L.SymSingleLongBox(54, 'H2')
        L.SymSingleLongBox(120, 'H3')
        L.SymSingleLongBox(3200, 'H4')
        L.SymSingleLongBox(70)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def PValueint():
    global i
    time.sleep(delay)
    try:
        L.NormSingleLongBox(683, 'L2')
        L.NormSingleLongBox(2439, 'L3')
        L.NormSingleLongBox(13432, 'L4')
        L.divinput2("Nine hundred and six", "L5")
        L.divinput2("Seven thousand, three hundred and twenty six", "L6")
        L.divinput2("Two thousand, nine hundred and thirteen", "L7")
        L.divinput2(40, "L8")
        L.divinput2(200, "L9")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "1357").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "7531").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()
        
        L.NormSingleLongBox(9025, 'H2')
        L.NormSingleLongBox(7073, 'H3')
        L.NormSingleLongBox(11018, 'H4')
        L.divinput2("Eighteen thousand, two hundred and nine", "H5")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[4]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[4]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "480000").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[9]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "3999997").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "3999900").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[10]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[10]/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def PVDecimals():
    global i
    time.sleep(delay)
    try:
        L.NormSingleLongBox('7/10', 'L2')
        L.NormSingleLongBox("1/5", 'H1')
        L.NormSingleLongBox('1/100', 'H2')
        L.NormSingleLongBox('1/125', 'H3')
        L.divinput2("tenths", "H4", "thousandths")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def PVMeaures():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "258.1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "2.581").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "700.6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "7.006").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "80").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "0.08").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "5.163").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()
        
        L.SymSingleLongBox(3000, 'H1')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "142.8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "1.428").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "86").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "0.86").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()
        
        L.SymSingleLongBox(0.78, 'H4')
        L.SymSingleLongBox(0.235)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def OrderInt():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "-5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "-4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "-6.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "-6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "-3.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "2.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        L.divinput2("-6", "H3", 5)
        L.divinput2(2, "H4")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "-23").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "-14").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "17").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "B").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "E").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "A").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "D").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def OrderDec():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(7.83, 'L2')
        L.SymSingleLongBox(6.2, 'L3')

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "9.115").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "9.15").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "9.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "13.136").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "13.36").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "13.6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "6.372").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "6.72").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "6.732").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "0.206").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "0.26").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "0.602").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "0.62").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "0.819").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "0.835").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "0.853").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "0.891").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "1.16").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "1.6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "6.116").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "6.12").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "6.2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "1.8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "8.1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "8.118").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "8.18").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "8.181").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "0.075").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "0.605").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "0.98").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "4.009").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "5.4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def IntMent():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "136").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "183").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "127").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "150").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "144").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "164").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "174").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "154").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "110").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "195").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "88").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "142").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "63").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "77").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "134").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "91").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "116").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "102").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "138").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "167").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2(63, "L4", 350)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "44").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "53").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "86").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "95").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "83").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "135").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "95").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "73").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "121").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "98").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "115").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "106").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "156").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "176").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "141").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "180").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "84").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "167").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "141").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "116").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "145").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "104").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "159").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "135").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2(25, "H4", 35, 45)
        L.divinput2("A", "H5", "21+22+23=66 while 20+19+18=57, and due to the insignificant invention of numeracy 57 is closer to 60 meaning set A is closer to 60")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "48").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "55").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "87").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "94").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        L.divinput2(6, "H7", 8)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()


    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def IntWrit():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[4]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[4]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[4]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[4]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "863").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "1622").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "1451").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "1569").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()
        L.divinput2(2, 0, 6, 5)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def SubIntMent():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "41").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "43").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "35").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "35").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "34").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "74").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "45").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "58").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "15").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "36").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "936").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "73").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "973").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "32").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "31").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "37").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "97").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()

        L.divinput2(80, "L8", 15)
        L.divinput2(399, "H1", 455)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "29").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "28").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "37").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "39").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "18").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "19").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "18").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "46").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "63").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "59").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "36").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "15").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[5]/input')
        actions.send_keys_to_element(water, "22").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[6]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[7]/input')
        actions.send_keys_to_element(water, "16").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[8]/input')
        actions.send_keys_to_element(water, "24").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[9]/input')
        actions.send_keys_to_element(water, "28").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[10]/input')
        actions.send_keys_to_element(water, "38").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2(9, "H4", 9, 41)
        L.divinput2(8, "H5", 8.5)
        L.divinput2(85, "H6", 33, 64)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "58").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "57").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "69").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "87").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[9]/a')
        actions.click(water).perform()

        L.divinput2(65, 0, 22)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def SubIntWrit():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        L.divinput2(5, "L5", 9, 6)
        L.divinput2(6, "H1", 1)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "249").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "476").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "345").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "436").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2(7, "H4", 5)
        L.divinput2(9, "H5", 6)
        L.divinput2(4, 0, 4, 7)    
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def MultEz():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "80").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "40").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "70").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "94").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "204").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "384").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "390").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "192").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "162").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "272").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "485").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "438").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "1704").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "2972").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "3135").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "1358").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "2358").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "3572").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "4345").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()
        L.divinput2(130, 0, 312)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def DivEz():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "238").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "229").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "145").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "62").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "289").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "163").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "169").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "57").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "÷10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "+10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "÷10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "÷10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "+10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        L.divinput2(26, 0, 8)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def UnitsLMC():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox(10, 'L2')
        L.SymSingleLongBox(100, 'L3')
        L.SymSingleLongBox(1000, 'L4')
        L.SymSingleLongBox(1000, 'L5')
        L.SymSingleLongBox(1000, 'L6')
        L.divinput2("A", "H1", 150)
        L.divinput2("metres", "H2", "kilograms")
        L.divinput2("millimetres", "H3", "kilometres")
        L.divinput2("litres", "H4", "millilitres")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()


    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def UTime():
    global i
    time.sleep(delay)
    try:
        L.SymSingleLongBox("09:00", "L2")
        L.SymSingleLongBox("05:35", "L3")
        L.SymSingleLongBox("20:00", "L4")
        L.SymSingleLongBox("19:55", "L5")
        L.divinput2("6 a.m.", "L6")
        L.divinput2("2:45 a.m.", "L7")
        L.divinput2("4 p.m.", "L8")
        L.divinput2("9:25 p.m.", "L9")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "4pm").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[12]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/forminput/formgroup/div/div/span/input')
        actions.send_keys_to_element(water, "9pm").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[13]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.SymSingleLongBox("49", "H2")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2("10:20 pm", "H4")
        L.divinput2("10:15 am", "H5", "1:20pm")
        L.divinput2("08:05", "H6", "47", "14:14")
        L.divinput2("8:27 pm", "H7")
        L.divinput2("35", "H8", "5:15")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "11").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "12").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "20").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def UMon():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "£6.52").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "£8.09").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "£13.40").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "£4.70").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, "£6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        L.NormSingleLongBox("£5.40", "L4")
        L.SymSingleLongBox(16.99, "L5")
        L.SymSingleLongBox(40, "L6")
        L.SymSingleLongBox(47, "L7")
        L.SymSingleLongBox("54.70", "H1")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "£6.70").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "9").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/forminput/formgroup/div/div/div/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "3.09").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "15.23").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "10").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "20").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, "50").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Reading():
    global i
    time.sleep(delay)
    try:
        L.divinput2(34, "L2")
        L.divinput2(27, "L3")
        L.divinput2(420, "L4")
        L.divinput2(230, "L5")
        L.divinput2(6.3, "L6")
        L.SymSingleLongBox(500, "L7")
        L.divinput2(48, "H1")
        L.divinput2(7.4, "H2")
        L.divinput2(1.3, "H3")
        L.SymSingleLongBox(250, "H6")
        L.divinput2(125, "H7", "-25")
        L.SymSingleLongBox(0.5, "H8")
        L.SymSingleLongBox(1.75, "H9")
        L.divinput2(450, 0)
        
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Symbols():
    global i
    time.sleep(delay)
    try:
        L.divinput2("<", "L2", "=", ">")
        L.divinput2(">", "H1", "<", "<")
        L.divinput2("A ≥ £850", "H2")
        L.divinput2("A ≤ 7", 0)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Factors():
    global i
    time.sleep(delay)
    try:
        L.divinput2("1,2,4,8", "L2")
        L.divinput2("1,2,3,6,9,18", "H1")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "Yes, because 12 is divisible by 4 to make 3. For example, if I had 12 imaginary kumquats and shared them equally between my 4 imaginary friends (I don't have any real ones) each one would have 3 imaginary kumquats.").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        L.divinput2("1,2,3,6", 0)


    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Multiples():
    global i
    time.sleep(delay)
    try:
        L.divinput2("6, 12, 18, 24, 30" ,"L2")
        L.NormSingleLongBox(30, "L3")
        
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "34").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "33").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "32").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.divinput2("1, 2, 4", "H2")
        L.divinput2(105, "H3", 112)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "58").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "57").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "56").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "55").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[3]/input')
        actions.send_keys_to_element(water, "54").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Patterns():
    global i
    time.sleep(delay)
    try:
        L.divinput2(18, "L2", 22)
        L.divinput2(-3, "L3", -9)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "22").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "31").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()
        
        L.divinput2(3, "L5")
        L.divinput2(6, "L6")
        L.divinput2(23, "L7", 29)
        L.divinput2(1, "L8", "-4")
        L.divinput2(0, "L9", 4)
        L.divinput2("-4", "H1", "-11")
        L.divinput2(33, "H2", 42)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "48").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "192").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2(26, "H4", 80)
        L.divinput2(18, 0, 4)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()
    
def HardAdd():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "0").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.NormSingleLongBox(5385, "H2")
        L.NormSingleLongBox(8140, "H3")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "157230").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "110958").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    
   
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()
    



def Primary():
    GettoPage()
    # CoordsQ1()#1
    # CoordsQ4()#2
    # AlgebraicVocab()#3
    # FormulaInWords()#4
    # AlgebraicNotation()#5
    # HIV_Lines()#6
    # LikeTerms()#7
    # AlgSimMult()#8
    # AlgSimDiv()#9
    # ExpandingBrackets()#10
    # Factorisation()#11
    # Substitution()#12
    # SeqTtT()#13
    # SeqPtS()#14
    # findNTerm()#15
    # GeometricDef()#16
    # CircleProp()#17






    # CountingSquares()#24
    # PeriFormula()#25
    # CountingAreaSquares()#26
    # BeginnerAngles()#27
    # NotMeasuringAngles()#28

    # Polygons()#30
    # TreeDProps()#31
    # TreeDModels()#32
    # TreeDNets()#33
    # AngleFacts()#34
    # PropsofQuads()#35

    # SpecialTriangles()#37
    TriAngleCalc()#38
    # AnglePara()#39
    # PolySums()#40
    # RectArea()#41
    # ParArea()#42
    # TriArea()#43
    # TrapArea()#44
    # PValueint()#45
    # PVDecimals()#46
    # PVMeaures()#47
    # OrderInt()#48
    # OrderDec()#49
    # IntMent()#50
    # IntWrit()#51
    # SubIntMent()#52
    # SubIntWrit()#53
    # MultEz()#54
    # DivEz()#55
    # UnitsLMC()#56
    # UTime()#57
    # UMon()#58
    # Reading()#59
    # Symbols()#60
    # Factors()#61
    # Multiples()#62
    # Patterns()#63
    # HardAdd()#64
Primary()
