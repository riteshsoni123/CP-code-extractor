from re import T
from selenium import webdriver
import time
import os 
import pyperclip as pc
from selenium.webdriver.common.by import By


main_dir = "C:/Users/comed/Desktop/codeforces/"

driver=webdriver.Chrome()

# driver.get('https://codeforces.com/submissions/demo_user')
driver.get('https://codeforces.com/submissions/Akash_Dixit27')

time.sleep(2)

for i in range(2,29):
    codeId=driver.find_element(By.XPATH,'//*[@id="pageContent"]/div[4]/div[6]/table/tbody/tr['+str(i)+']/td[1]/a')
    codeId.click()

    time.sleep(2)

    names=driver.find_element(By.XPATH,'//*[@id="facebox"]/div/div/div/span').text
    print(names)
    contestName=''
    QuestionName=''
    verdict='Wrong'
    startIndex=-1
    endIndex=-1
    for j in range(len(names)):
        if names[j]==':':
            startIndex=startIndex=j+2

        if names[j]==',' and startIndex!=-1:
            endIndex=j

        if startIndex !=-1 and endIndex !=-1:
            contestName=names[startIndex:endIndex]
            break


    startIndex=-1
    endIndex=-1

    for j in range(len(names)):
        if names[j]==':' and names[j+2]=='(':
            startIndex=j+2
            
        if names[j]==',' and startIndex!=-1:
            endIndex=j

        if startIndex !=-1 and endIndex !=-1:
            QuestionName=names[startIndex:endIndex]
            break

    for j in range(len(names)-9):
        if names[j:j+8] == 'Accepted':
            verdict='Accepted'
            break
    
    unUsedCharacter=['\\','/',':','*','?','"','<','>','|']

    temp=''
    for j in contestName:
        flag=True
        for k in unUsedCharacter:
            if j==k:
                flag=False
                break
        if flag:
            temp=temp+str(j)

    contestName=temp
    temp=''

    for j in QuestionName:
        flag=True
        for k in unUsedCharacter:
            if j==k:
                flag=False
                break
        if flag:
            temp=temp+str(j)

    QuestionName=temp

    print(contestName)
    print(QuestionName)
    print(verdict)

    if verdict == 'Wrong':
        driver.find_element(By.XPATH,'//*[@id="facebox"]/div/a/img').click()
        time.sleep(0.5)
        print('******************************************  '+str(i)+'  ******************************************')
        continue

    if not os.path.isdir(main_dir+contestName+"/"):
        os.mkdir(main_dir+contestName)
    
    if os.path.isfile(main_dir+contestName+"/"+QuestionName+'.cpp'):
        continue

    f = open(main_dir+contestName+"/"+QuestionName+'.cpp',"a")
    time.sleep(0.5)
    for j in range(1,1000):
        try:
            store=driver.find_element(By.XPATH,'//*[@id="facebox"]/div/div/div/pre/code/ol/li['+str(j)+']').text
            f.write(store+"\n")
        except:
            break
    f.close()

    driver.find_element(By.XPATH,'//*[@id="facebox"]/div/a/img').click()
    time.sleep(0.5)
    print('******************************************  '+str(i)+'  ******************************************')


