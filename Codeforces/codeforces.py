from audioop import cross
from pydoc import cli
from re import T
from idna import valid_label_length
from selenium import webdriver
import time
import os 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By


main_dir = "C:/Users/comed/Desktop/codeforces/"
driver=webdriver.Chrome()

def call_element(driver,xpath):
    current_element=''
    try:
        current_element=ui.WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath)))
    except:
        if len(xpath)>52 and xpath[0:52]=='//*[@id="pageContent"]/div[4]/div[6]/table/tbody/tr[':
            return 'next_page'
        else:
            print(xpath)
            driver.quit()
    return current_element

def write_code(contestName,QuestionName):
    if not os.path.isdir(main_dir+contestName+"/"):
        os.mkdir(main_dir+contestName)
        
    if os.path.isfile(main_dir+contestName+"/"+QuestionName+'.cpp'):
        return False

    f = open(main_dir+contestName+"/"+QuestionName+'.cpp',"a")

    for j in range(1,1000):
        try:
            store=driver.find_element(By.XPATH,'//*[@id="facebox"]/div/div/div/pre/code/ol/li['+str(j)+']').text
            f.write(store+"\n")
        except:
            break
    f.close()
    return True

def filter_name(f_name):
    unUsedCharacter=['\\','/',':','*','?','"','<','>','|']
    temp=''
    for j in f_name:
        flag=True
        for k in unUsedCharacter:
            if j==k:
                flag=False
                break
        if flag:
            temp=temp+str(j)
    return temp

def extract_contest_name(names):
    startIndex=-1
    endIndex=-1
    for j in range(len(names)):
        if names[j]==':':
            startIndex=startIndex=j+2

        if names[j]==',' and startIndex!=-1:
            endIndex=j

        if startIndex !=-1 and endIndex !=-1:
            return filter_name(names[startIndex:endIndex])

def extract_question_name(names):
    startIndex=-1
    endIndex=-1
    for j in range(len(names)):
        if names[j]==':' and names[j+2]=='(':
            startIndex=j+2
            
        if names[j]==',' and startIndex!=-1:
            endIndex=j

        if startIndex !=-1 and endIndex !=-1:
            return filter_name(names[startIndex:endIndex])

def extract_verdict(names):
    for j in range(len(names)-9):
        if names[j:j+8] == 'Accepted':
            return 'Accepted'
    return 'Wrong'

for p in range(1,200):
    driver.get('https://codeforces.com/submissions/ritesh_soni123/page/'+str(p))
    time.sleep(2)

    for i in range(51,1000):
        codeId=call_element(driver,'//*[@id="pageContent"]/div[4]/div[6]/table/tbody/tr['+str(i)+']/td[1]/a')
        if codeId=='next_page':
            break
        codeId.click()

        names=call_element(driver,'//*[@id="facebox"]/div/div/div/span').text
        print(names)
        contestName=extract_contest_name(names)
        QuestionName=extract_question_name(names)
        verdict=extract_verdict(names)

        print(contestName)
        print(QuestionName)
        print(verdict)

        if verdict == 'Wrong':
            call_element(driver,'//*[@id="facebox"]/div/a/img').click()
            print('***************************Page= '+str(p)+' Question= '+str(i)+'  ***************************')
            continue

        if write_code(contestName,QuestionName):
            call_element(driver,'//*[@id="facebox"]/div/a/img').click()
            print('**********************Page= '+str(p)+' Question= '+str(i)+'  ***********************')

        


