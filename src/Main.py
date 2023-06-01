MakeLog = 1 #Make this an on/off option in the GUI
if MakeLog == 1:
    import sys
    import os
    if os.path.exists("MSB.log"):
        os.remove("MSB.log")
    sys.stdout = open("MSB.log", "w")
import time
from Driver import driver
from Driver import actions
from Driver import By
from Driver import Select
import Layouts as L
#Everything is imported from Driver so that only 1 instance of Selenium is created
#The current set of questions being worked on is 95
i=95
delay = 0.5

def GettoPage():
    #This takes the user to the My Progress page and is indented to enter each task once the previous one has been finished
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
    #Allow people with smaller screens by loading the website again but changing the URL to the next question as each question has a unique URL
    #Make it MultiFile to make myself look like a competent programmer ./ Success!
    #Maybe publish it on Github ./ Done, It is now publically open source
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
        L.SymLongBox(94, 'L2')
        L.SymLongBox(9, 'H1')
        L.SymLongBox(1.5, 'H2')
        L.SymLongBox(11)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def AlgebraicNotation():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox('4x+5', 'L2')
        L.NormLongBox('2x-9', 'L3')
        L.NormLongBox('2(x-4)', 'L4')
        L.NormLongBox('6(x+2)', 'H1')
        L.NormLongBox('3(2x-5)', 'H2')
        L.NormLongBox("x^2 + 4", 'H3')
        L.NormLongBox("(4x+1)^2")

    except:
        print("3rr0r", i)
    finally:        
        i+=1
        GettoPage()

def HIV_Lines():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox("x=4", "L2", "y=7")
        L.SymLongBox("y=1", "L3", "x=2")
        L.SymLongBox("y=1.5", "H1", "x=8.5")
        L.SymLongBox("x=4.5", 0, "y=-2")
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def LikeTerms():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox("10a", "L2", "7x", "7p")
        L.NormLongBox("8x+7y", "L3", "4x+3y")
        L.NormLongBox("8x+8a", "L4", "2p+6q")
        L.NormLongBox("8a+3x", "L5", 0)

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
        
        L.NormLongBox("11x-5y", "H2")
        L.NormLongBox("6x-4y", "H3")
        L.NormLongBox("x-7y", "H4")
        L.NormLongBox("4x^2 t+11xy")

    except:
        print("3rr0r", i)
    finally:     
        i += 1
        GettoPage()

def AlgSimMult():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox("6x", "L2", "8xy", "12xy")
        L.NormLongBox("10xy", "L3", "24pqr")
        L.NormLongBox("x^4", "L4", "y^6")
        L.NormLongBox("x^4 y^2", "L5", "12x^3 y^5")
        L.NormLongBox("x^7", "L6", "y^7")
        L.NormLongBox("x^9", "H1", 0)
        L.NormLongBox("3x^8", "H2", 0)
        L.NormLongBox("20x^8", "H3", 0)
        L.NormLongBox("10x^5 y^9", "H4", 0)
        L.NormLongBox("32x^4 y^6", 0, 0)
    except:
        print("3rr0r", i)
    finally:
        i += 1
        GettoPage()

def AlgSimDiv():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox("x^4", "L2", "y")
        L.NormLongBox("3x^2", "L3", "6y^6")
        L.NormLongBox("x^3", "L4", "y")
        L.NormLongBox("8x^5", "H1", 0)
        L.NormLongBox("3c^4 d^3", "H2", "4a^3 b^4")
        L.NormLongBox(1, "H3", 0)
        L.NormLongBox("8x^2 y", "H4", "10y^3")
        L.NormLongBox("8/y", "H5", "6y")
        L.NormLongBox("2xy", 0, "4y^2")
    except:
        print("3rr0r", i)
    finally:      
        i += 1
        GettoPage()
    
def ExpandingBrackets():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox("4x+12", 'L2')
        L.NormLongBox("12x+9", 'L3')
        L.NormLongBox("14x-21", 'L4')
        L.NormLongBox("4x^2 + 3x", 'L5')
        L.NormLongBox("12x^2 - 15x", 'H1')
        L.NormLongBox("8x^2 + 6xy", 'H2')
        L.NormLongBox("5p^2 - 15pq", 'H3')

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
        L.NormLongBox("3(3x+2)", 'L2')
        L.NormLongBox("6(x+2)", "L3")
        L.NormLongBox("7(2x-3)", "L4")
        L.NormLongBox("y(y-1)", 'L5')
        L.NormLongBox("P^2 (p+1)", "L6")
        L.NormLongBox("y(y^2 -1)", 'H1')
        L.NormLongBox("3x(x+3)", "H2")
        L.NormLongBox("5x(2x-1)", "H3")
        L.NormLongBox("x^2 (5+x)", 'H4')
        L.NormLongBox("5x^2 (3x-2)", 'H5')
        L.NormLongBox("2t(8t^2 +5)", "H6")
        L.NormLongBox("4y(xy+2)", "H7")
        L.NormLongBox("3xy(2x+5y)")
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Substitution():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(13, "L2", 24, 4)
        L.NormLongBox(49, "L3", 100)
        L.NormLongBox(4, "L4", 18, 24, 16)

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
        
        L.SymLongBox(11, "H1", "-9")
        L.SymLongBox("-10", "H2", 25, 75)
        L.NormLongBox(25, "H3", 100, 4, 625)
        L.NormLongBox(36, 0, 5, 1296)
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
        L.NormLongBox('3n', 'L2')
        L.NormLongBox('2n+5', 'L3')
        L.divinput2(26, "L4", "4n+2")
        L.divinput2(19, "H1", "3n+1")
        L.NormLongBox('9n-8', 'H2')
        L.NormLongBox('20-2n')

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
        L.SymLongBox(20, 'L2')
        L.SymLongBox(20, 'H1')
        L.SymLongBox(22, 'H2')
        L.SymLongBox(26)
    except:
        print("3rr0r", i)
    finally:
        i += 1
        GettoPage()

def PeriFormula():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox(24, 'L2')
        L.SymLongBox(28, 'L3')
        L.SymLongBox(49.8, 'H1')
        L.SymLongBox(8, 'H2')
        L.SymLongBox(17.15, 'H3')
        L.SymLongBox(6.5)
    except:
        print("3rr0r", i)
    finally:
        i += 1
        GettoPage()

def CountingAreaSquares():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox(25, 'L2')
        L.SymLongBox(32, 'H1')
        L.SymLongBox(27, 'H2')
        L.SymLongBox(15.75, 'H3')
        L.SymLongBox(8, 'H4')
        L.SymLongBox(18)
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
        L.SymLongBox(30, "L2")
        L.SymLongBox(140, "H1")
        L.SymLongBox(210, "H2")
        L.SymLongBox(320, "H3")

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
        L.SymLongBox(75, 'L3')
        L.SymLongBox(34, 'L4')
        L.SymLongBox(125, 'L5')

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
        
        L.SymLongBox(121, 'H2')
        L.SymLongBox(110, 'H3')

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
        L.SymLongBox(70, 'L2')
        L.SymLongBox(50, 'L3')
        L.SymLongBox(70, 'L4')
        L.SymLongBox(55, 'L5')
        L.SymLongBox(115, 'L6')
        L.divinput2("No because due to simple mathmatics they don't add up to 180", "L7")
        L.SymLongBox(120, 'L8')
        L.SymLongBox(40, 'L9')
        L.divinput2("No", "H1", "The angles don't add up to 180")
        L.SymLongBox(120, 'H2')
        L.SymLongBox(90, "H3", 25, 25)
        L.SymLongBox(60, "H4", 120, 35)
        L.SymLongBox(72, "H5", 36, 38)
        L.SymLongBox(90, "H6", 40, 40)

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
        L.SymLongBox(70, 'L2')
        L.SymLongBox(110, 'L3')
        L.SymLongBox(110, 'L4')
        L.SymLongBox(75, 'L5')
        L.SymLongBox(72, 'H1')
        L.SymLongBox(73, 'H2')
        L.SymLongBox(30, 'H3')
        L.SymLongBox(70, "H4", 80, 30)
        L.SymLongBox(52, "L5", 58)
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
        L.SymLongBox(1080, 'L2')
        L.SymLongBox(900, 'L3')
        L.SymLongBox(140, 'L4')
        L.SymLongBox(720, "L5", 120)
        L.SymLongBox(135, "H1", 45)

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
        L.SymLongBox(20, 'L2')

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
        
        L.SymLongBox(10, 'L5')
        L.divinput2("Yes", "L6", "Shape B is 6 squares. Shape A is 12 squares which is double 6 squares")
        L.divinput2("B", "H1", "Shape A is 10 squares. Shape B is 12 squares. You can just count the squares")
        L.NormLongBox(9, 'H2')
        L.SymLongBox(25, 'H3')
        L.SymLongBox(49, 'H4')
        L.SymLongBox(50, 'H5')
        L.SymLongBox(75, 'H6')

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
        
        L.SymLongBox(8, "H8", 2.6)

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
        L.SymLongBox(80, 'L2')
        L.SymLongBox(27.9, 'L3')
        L.SymLongBox(36, 'H1')
        L.SymLongBox(128, 'H2')
        L.SymLongBox(92.3, 'H3')
        L.SymLongBox(15, "H4", 18)

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
        L.SymLongBox(27, 'L2')
        L.SymLongBox(20.58, 'L3')
        L.SymLongBox(24, 'L4')
        L.SymLongBox(210, 'L5')

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
        L.SymLongBox(50, 0, 10, 10, 30)
    except:
        print("3rr0r", i)
    finally:
        i+=1 
        GettoPage()

def TrapArea():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox(20, 'L2')
        L.SymLongBox(24, 'L3')
        L.SymLongBox(20, 'L4')
        L.SymLongBox(8, "L5", 4, 16)
        L.SymLongBox(8, "H1", 2, 8)
        L.SymLongBox(54, 'H2')
        L.SymLongBox(120, 'H3')
        L.SymLongBox(3200, 'H4')
        L.SymLongBox(70)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def PValueint():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(683, 'L2')
        L.NormLongBox(2439, 'L3')
        L.NormLongBox(13432, 'L4')
        L.divinput2("Nine hundred and six", "L5")
        L.divinput2("Seven thousand, three hundred and twenty six", "L6")
        L.divinput2("Two thousand, nine hundred and thirteen", "L7")
        L.divinput2(40, "L8")
        L.divinput2(200, "L9")
        L.SymLongBox(1357, "H1", 7531) 
        L.NormLongBox(9025, 'H2')
        L.NormLongBox(7073, 'H3')
        L.NormLongBox(11018, 'H4')
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
        
        L.NormLongBox("3999997", "H8", "3999900")

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
        L.NormLongBox('7/10', 'L2')
        L.NormLongBox("1/5", 'H1')
        L.NormLongBox('1/100', 'H2')
        L.NormLongBox('1/125', 'H3')
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
        
        L.SymLongBox(3000, 'H1')
        L.SymLongBox(142.8, "H2", 1.428)
        L.SymLongBox(86, "H3", 0.86)
        L.SymLongBox(0.78, 'H4')
        L.SymLongBox(0.235)

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
        L.SymLongBox(7.83, 'L2')
        L.SymLongBox(6.2, 'L3')

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
        
        L.NormLongBox(863, "H2", 1622)
        L.NormLongBox(1451, "H3", 1569)
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
        
        L.NormLongBox(36, "L4", 936)
        L.NormLongBox(73, "L5", 973)

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
        L.NormLongBox(249, "H2", 476)
        L.NormLongBox(345, "H3", 436)
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
        
        L.NormLongBox(80, "H1", 40, 70)
        L.NormLongBox(94, "H2", 204, 384, 390)
        L.NormLongBox(192, "H3", 162, 272, 485)
        L.NormLongBox(438, "H4", 1704, 2972, 3135)
        L.NormLongBox(1358, "H5", 2358, 3572, 4345)
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
        
        L.NormLongBox(238, "H4", 229, 145, 62)
        L.NormLongBox(289, "H5", 163, 169, 57)

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
        L.SymLongBox(10, 'L2')
        L.SymLongBox(100, 'L3')
        L.SymLongBox(1000, 'L4')
        L.SymLongBox(1000, 'L5')
        L.SymLongBox(1000, 'L6')
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
        L.SymLongBox("09:00", "L2")
        L.SymLongBox("05:35", "L3")
        L.SymLongBox("20:00", "L4")
        L.SymLongBox("19:55", "L5")
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

        L.SymLongBox("49", "H2")

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
        L.NormLongBox("£6.52", "L2", "£8.09", "£13.40")
        L.NormLongBox("£4.70", "L3", "£6")
        L.NormLongBox("£5.40", "L4")
        L.SymLongBox(16.99, "L5")
        L.SymLongBox(40, "L6")
        L.SymLongBox(47, "L7")
        L.SymLongBox("54.70", "H1")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "£6.70").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        L.SymLongBox(9, "H3", 4)

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
        L.SymLongBox(500, "L7")
        L.divinput2(48, "H1")
        L.divinput2(7.4, "H2")
        L.divinput2(1.3, "H3")
        L.SymLongBox(250, "H6")
        L.divinput2(125, "H7", "-25")
        L.SymLongBox(0.5, "H8")
        L.SymLongBox(1.75, "H9")
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
        L.NormLongBox(30, "L3")
        
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

        L.NormLongBox(5385, "H2")
        L.NormLongBox(8140, "H3")
        L.NormLongBox(157230, 0, 110958)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()
    
def DecAdd():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        L.NormLongBox(41.3, "L3")
        L.NormLongBox(41.7, "L4")
        L.NormLongBox(136.15, "L5")
        L.NormLongBox(650.21, "L6")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "4.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "0.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "0.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "0.5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[2]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.NormLongBox(153.78, "H2")
        L.NormLongBox(123.294, "H3")
        L.NormLongBox(321.006, 0)



    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()
    
def HardSub():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.NormLongBox(6288, "H2")
        L.NormLongBox(2876, "H3")
        L.NormLongBox(6355, "H4")
        L.NormLongBox(4853, 0)


    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def DecSub():
    global i
    time.sleep(delay)
    try:

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "2").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        L.NormLongBox(61.34, "L4")
        L.NormLongBox(431.72, "L5")
        L.divinput2(6.2, "H1")
        L.NormLongBox(7.588, "H2")
        L.NormLongBox(24.67, "H3")
        L.NormLongBox(215.76, "H4")
        L.divinput2(12.3, "H5")
        L.NormLongBox(25.62, "H6")
        L.divinput2(1.59, 0)

    
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def ShMultInt():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(96, "L2")
        L.NormLongBox(116, "L3")
        L.NormLongBox(228, "L4")
        L.NormLongBox(702, "L5")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "11").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "28").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "8").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "48").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "11").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "48").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "36").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "56").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "99").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "12").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.NormLongBox(1023, "H2")
        L.NormLongBox(1036, "H3")
        L.NormLongBox(2655, "H4")
        L.NormLongBox(4544, "H5")
        
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[3]/div/subtag/div/div/div/div[6]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[4]/div/subtag/div/div/div/div[3]/div')
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

def ShMultDec():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(7.2, "L2")
        L.NormLongBox(16.2, "L3")
        L.NormLongBox(60.2, "L4")
        L.NormLongBox(7.2, "H1")
        L.NormLongBox(7.29, "H2")
        L.NormLongBox(74, "H3")
        L.NormLongBox(0.96, "H4")
        L.NormLongBox(6.93, 0)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def SDIntegers():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "1").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        L.NormLongBox(73, "L3")
        L.NormLongBox(89, "L4")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "17").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "60").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "17").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "14").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "12").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.NormLongBox(225, "H2")
        L.NormLongBox(573, "H3")
        L.NormLongBox(3683, "H4")
        L.SymLongBox(95, 0)


    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def POT():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(80, "L2", 0.8)
        L.NormLongBox(620, "L3", 6.2)
        L.NormLongBox(2690, "H1", 87.3)
        L.NormLongBox(58800, "H2", 5.88)
        L.NormLongBox(66200, "H3", 3.7)
        L.NormLongBox(476000, "H4", 0.003)
        L.divinput2("Balnamore", 0, "Longton", "1000")
    
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def POTDec():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(36, "L2", 0.36)
        L.NormLongBox(1520, "L3", 0.152)
        L.NormLongBox(287300, "H1", 0.2873)
        L.NormLongBox(0.4, "H2", 0.008)
        L.NormLongBox(0.07, "H3", 0.02714)
        L.NormLongBox(6310, "H4", 490)
        L.divinput2(100, 0, 1000)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def NegativesIRL():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox("-6", "L2")
        L.SymLongBox(7, "L3")
        L.divinput2(7, "H1", "-6")
        L.divinput2("Dundee", "H2", 8, "Dundee")
        L.divinput2(60, "H3", "-40", 22, "-11")
        L.divinput2("Friday", 0, 5)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def DirectedNumbers():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "B").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "D").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "C").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "A").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()
        
        L.divinput2("-4", "L3", "-11", 3)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "17").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "-3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "25").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "11").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        L.divinput2("5 3/4", "H1", "-3")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "D").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "A").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "C").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, "B").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        L.divinput2(8, "H3", 3, "-3")
        L.divinput2(5, "H4", 4)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "13").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "6").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "-7").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "-5").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, "4").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
    
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def DirectedNumbers2():
    global i
    time.sleep(delay)
    try:
        L.divinput2("-18", "L2", "-20", "14")
        L.divinput2("-2", "H1", "-8", "6")
        L.divinput2("-30", "H2", 24, "-35")
        L.divinput2("-3", "H3", "-21", "-30")
        L.divinput2("-35", 0, "-4")

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def BODMAS():
    global i
    time.sleep(delay)
    try:
        L.divinput2(11, "L2", 14)
        L.divinput2(29, "L3", 100)
        L.divinput2(11, "L4", 7)
        L.divinput2(50, "L5", 100)
        L.divinput2(24, "H1", 8)
        L.NormLongBox(28, "H2", 32, 4)
        L.NormLongBox(5, "H3", 62)
        L.divinput2(2, "H4", 99)
        L.divinput2(101, "H5", 1800)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "-").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "-").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "+").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "+").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "-").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "+").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "+").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "-").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, "x").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "x").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "+").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, "-").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def DisTables():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox(150, "L2", "Sheffield, Cambridge", 161)
        L.SymLongBox(73, "H1", "York", 162)
        L.SymLongBox(107, "H2", "Halifax", 61)
        L.SymLongBox(583, 0, 485)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def TimeTables():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox("0854", "L2", 21)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, "0955").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 0).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, 35).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, 25).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, 48).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 8).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, 50).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[1]/input')
        actions.send_keys_to_element(water, 11).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div[2]/input')
        actions.send_keys_to_element(water, "04").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/input')
        actions.send_keys_to_element(water, 49).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 11).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "03").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, 1613).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 38).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 38).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def IRLProblems():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox("3.60", "L2")
        L.SymLongBox("2.50", "L3")
        L.divinput2(10.75, "L4")
        L.SymLongBox(43, "L5")
        L.SymLongBox(61, "L6")
        L.divinput2(22, "L7")
        L.divinput2("0.90", "L8")
        L.divinput2(40, "H1")
        L.divinput2(15, "H2", "25p")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "Website B by 47p").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[5]/a')
        actions.click(water).perform()

        L.divinput2("£0.28", "H4")
        L.divinput2(3.95, 0, "0.50")

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def IRLCalc():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox(3712, "L2")
        L.SymLongBox(242500, "L3")
        L.SymLongBox(206500, "L4")
        L.SymLongBox("4113.70", "L5")
        L.divinput2("1.20", "H1")
        L.SymLongBox(2740, "H2")
        L.SymLongBox(140712, "H3")
        L.NormLongBox(8, "H4", 61600)
        L.SymLongBox(149, "H5", 14)
        L.NormLongBox(2941, "H6", 4761)
        L.divinput2("£40.80", "H7", 8)
        L.divinput2(20, 0, "217.50", 16.99, "627.20")

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def ShadowFractions():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox("1/3", "L2")
        L.NormLongBox("3/4", "L3")
        L.NormLongBox("1/5", "L4")
        L.NormLongBox("1/3", "H1")
        L.NormLongBox(6, "H2")
        L.NormLongBox(8, "H3")
        L.divinput2(5, "H4", 1)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()
        L.NormLongBox("2/3", 0, "2/3", "2/3")
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def EqFractions():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[1]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[3]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[4]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div/div/subtag/div/div/div/div[5]/div')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()
        
        L.divinput2(8, "L4")
        L.divinput2(15, "L5")
        L.divinput2(2, "L6", 6)
        L.divinput2(4, "H1", 18)
        L.divinput2(5, "H2")
        L.divinput2(5, "H3")
        L.divinput2(2, "H4", 30)
        L.divinput2(3, 0, 10)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def SimpFractions():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox("1/2", "L2")
        L.NormLongBox("3/5", "L3")
        L.NormLongBox("4/5", "H1")
        L.NormLongBox("3/4", "H2")
        L.NormLongBox("7/10", "H3")
        L.NormLongBox("7/20", 0)
    
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def IntroPercentages():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox(30, "L2")
        L.SymLongBox(55, "L3")
        L.SymLongBox(94, "H1")
        L.SymLongBox(76, "H2")
        L.SymLongBox(8, "H3")
        L.SymLongBox(41, 0)


    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def PercOfAmount():
    global i
    time.sleep(delay)
    try:
        L.SymLongBox(30, "L2", 15)
        L.SymLongBox(35, "L3", "17.50")
        L.SymLongBox("3.50", "L4")
        L.SymLongBox("1.9", "L5")
        L.SymLongBox("6.4", "L6")
        L.SymLongBox("24", "H1")
        L.SymLongBox("9", "H2")
        L.SymLongBox("3.90", "H3")
        L.SymLongBox("49", "H4")
        L.SymLongBox("51", "H5")
        L.NormLongBox(9, "H6", 27)

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 18).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 9).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, 1.8).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, 28.8).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[9]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 20).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, 0.4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, 22.4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[10]/a')
        actions.click(water).perform()

        L.divinput2(473, "H9")
        L.divinput2(60, 0)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Power():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(64, "L2")
        L.NormLongBox(100, "L3")
        L.NormLongBox(52, "L4")
        L.NormLongBox(125, "H1")
        L.NormLongBox(7, "H2")
        L.NormLongBox(2, "H3")
        L.NormLongBox(17, 0)
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def FunctionMachines():
    global i
    time.sleep(delay)
    try:
        L.divinput2(24, "L2", 13)
        L.divinput2(6, "L3", 9)
        L.divinput2(24, "H1", 18)
        L.divinput2(19, "H2")
        L.divinput2(8, "H3")
        L.divinput2(9, "H4")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, "D").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, "B").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, "A").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, "D").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[7]/a')
        actions.click(water).perform()

        L.divinput2(17, 0)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Rounding():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(60, "L2", 240, 480)
        L.NormLongBox(400, "L3", 2800, 5400)
        L.NormLongBox(6000, "L4", 138000, 79000)
        L.divinput2(87700, "H1", 8800, 900)
        L.NormLongBox(1630, "H2", 2930) 
        L.NormLongBox(8300, "H3", 1700)
        L.NormLongBox(143000, "H4", 263000)
        L.divinput2(40800, 0, 4100, 400)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def RoundingDec():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(53.8, "L2", 0)
        L.NormLongBox(422.7, "L3", 0)
        L.NormLongBox(89.3, "L4", 0)
        L.NormLongBox(0.72, "L5", 0)
        L.NormLongBox(8.84, "L6", 0)
        L.NormLongBox(8.84, "H1", 0)
        L.NormLongBox("37.0", "H2", 0)
        L.NormLongBox("23.30", "H3", 0)
        L.NormLongBox("5.00", "H4", 0)
        
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, "3.1416").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/div/div/div[1]/div')
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

def LongMult():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 1).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 0).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, 3).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, 0).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, 0).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, 5).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 7).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, 4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 8).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, 0).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[4]/input')
        actions.send_keys_to_element(water, 1).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, 5).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 5).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, 4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[5]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, 3).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, 8).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, 0).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, 0).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[4]/input')
        actions.send_keys_to_element(water, 4).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[6]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 3).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, 9).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, 3).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[4]/input')
        actions.send_keys_to_element(water, 9).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, 6).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, 7).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[7]/a')
        actions.click(water).perform()
        
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, 874).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, 2.28).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[8]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[1]/div/subtag/div/formgroup/div/div/span/div/div[1]')
        actions.send_keys_to_element(water, 1692).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/formhorizontal/form/div[2]/div/subtag/div/formgroup/div/div/div/div/div[1]')
        actions.send_keys_to_element(water, 10.92).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[9]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 100).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 20).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[1]/input')
        actions.send_keys_to_element(water, 400).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[2]/input')
        actions.send_keys_to_element(water, 600).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[3]/input')
        actions.send_keys_to_element(water, 120).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div[4]/input')
        actions.send_keys_to_element(water, 18).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[4]/div/input')
        actions.send_keys_to_element(water, 3198).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[10]/a')
        actions.click(water).perform()

        L.divinput2(1800, "H1", 1440)
        L.NormLongBox(3915, "H2")
        L.NormLongBox(4536, "H3")
        L.NormLongBox(20861, "H4")
        L.SymLongBox(864, "H5")
        L.SymLongBox(984, "H6")
        L.divinput2(3510, 0)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def LongMultDec():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(30.1, "L2", 2.82)
        L.SymLongBox(41.3, "L3")
        L.SymLongBox("187.20", "L4")
        L.NormLongBox(11.2, "H1", 2.22)
        L.NormLongBox(12.88, "H2", 0.0322)
        L.NormLongBox(15.58, 0, 0.0516)
        
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def LongDiv():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(34, "L2")
        L.NormLongBox(52, "L3")
        L.NormLongBox(64, "L4")
        L.NormLongBox(123, "L5")
        L.SymLongBox(17, "L6")
        L.SymLongBox(109, "L7")
        L.divinput2(153, "H1")
        L.NormLongBox(32.5, "H2")
        L.NormLongBox(19.2, "H3")
        L.NormLongBox(35.25, "H4")
        L.NormLongBox(20.5, "H5")
        L.NormLongBox(24.25, "H6")
        L.NormLongBox(24.75, 0)

    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def LongDivDec():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(2.6, "L2", 0)
        L.NormLongBox(4.9, "L3", 0)
        L.NormLongBox(0.89, "H1", 0)
        L.NormLongBox(4.13, "H2", 0)
        L.NormLongBox(7.8, "H3", 0)
        L.NormLongBox(3.06, 0, 0)
        
        
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()

def Prime():
    global i
    time.sleep(delay)
    try:
        L.NormLongBox(2, "L2", 0)
        L.NormLongBox(5, "L3", 0)
        L.divinput2("11, 13", "L4")
        L.divinput2("3, 5, 7", "H1")
        L.divinput2("2, 3, 5, 7", "H2")
        L.divinput2("5, 7, 11, 13", "H3")
        L.divinput2(1, "H4", "5 is a prime number, just a quick guess")

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div/textarea')
        actions.send_keys_to_element(water, "After an hour with a calculator, I have found that 27 is divisible by 3 and 9. Since it is divisible by a number other than 1 and itself, it is not a prime number.").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()


        
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage() 

def PrimeFactors():
    global i
    time.sleep(delay)
    try:
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 12).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 6).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[4]/input')
        actions.send_keys_to_element(water, 2).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "2x2x2x3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[1]/ul/li[4]/a')
        actions.click(water).perform()

        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[1]/input')
        actions.send_keys_to_element(water, 9).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[2]/input')
        actions.send_keys_to_element(water, 3).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[2]/div[3]/input')
        actions.send_keys_to_element(water, 3).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[1]/div[3]/div/input')
        actions.send_keys_to_element(water, "2x3x3").perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[4]/div/div[2]/answer/div/div/div/button')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/toaster/div/a')
        actions.click(water).perform()
        water = driver.find_element(by=By.XPATH, value='/html/body/app/main/div[2]/routehandler/div/div[1]/div/panel/div/div[3]/div[3]/ul/li[3]/a')
        actions.click(water).perform()

        L.divinput2("2 × 5 × 5", "H2")
        L.divinput2("2 × 3 × 3 × 5", 0)
        
    except:
        print("3rr0r", i)
    finally:
        i+=1
        GettoPage()



def Primary():
    Myth = time.time()
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
    # TriAngleCalc()#38
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
    # DecAdd()#65
    # HardSub()#66
    # DecSub()#67
    # ShMultInt()#68
    # ShMultDec()#69
    # SDIntegers()#70
    # POT()#71
    # POTDec()#72
    # NegativesIRL()#73
    # DirectedNumbers()#74
    # DirectedNumbers2()#75
    # BODMAS()#76
    # DisTables()#77
    # TimeTables()#78
    # IRLProblems()#79
    # IRLCalc()#80
    # ShadowFractions()#81
    # EqFractions()#82
    # SimpFractions()#83
    # IntroPercentages()#84
    # PercOfAmount()#85
    # Power()#86
    # FunctionMachines()#87
    # Rounding()#88
    # RoundingDec()#89
    # LongMult()#90
    # LongMultDec()#91
    # LongDiv()#92
    # LongDivDec()#93
    # Prime()#94
    PrimeFactors()#95
    print(time.time() - Myth)

Primary()

if MakeLog == 1:
    sys.stdout.close()

##### Template for functions #####
    # global i
    # time.sleep(delay)
    # try:

        
    # except:
    #     print("3rr0r", i)
    # finally:
    #     i+=1
    #     GettoPage()
##################################