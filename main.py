# imports here
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

# these are the driver varialbes, change "path" to where the chromedriver is located on your computer.
path = "D:\\python_automation\\google_bot\\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

# user input
searchup = input("what would you like to search? ")

def searching_google(x):
    # searching for the varialbe "searchup" which contains the input before running the script, on google
    driver.get("https://www.google.com")
    time.sleep(2.4)
    searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    searchbox.send_keys(searchup)
    searchbox.send_keys(Keys.ENTER)
    flnp_google()

def flnp_google():
    time.sleep(2.4)
    # finding links, putting them in a list and then printing it out
    links = []
    for x in range(1, 6):
        # goes through the results and adds the first 8 links to the list, if it has an error it will add less then five.
        try:
            links.append(driver.find_element_by_xpath('//*[@id="rso"]/div['+ str(x) +']/div/div[1]/a').get_attribute('href'))
        except NoSuchElementException:
            x = x + 1
    #prints the list
    print("Google Results:" + str(links))
    time.sleep(1.0)
    searching_bing()

def searching_bing():
    # searching for the varialbe "searchup" which contains the input before running the script, on google
    driver.get("https://www.bing.com")
    time.sleep(2.4)
    searchbox = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
    searchbox.send_keys(searchup)
    searchbox.send_keys(Keys.ENTER)
    flnp_bing()

def flnp_bing():
    time.sleep(2.4)
    # finding links, putting them in a list and then printing it out
    links = []
    for x in range(1, 6):
        # goes through the results and adds the first 5 links to the list
        try:
            links.append(driver.find_element_by_xpath('/html/body/div[1]/main/ol/li[' + str(x) + ']/h2/a').get_attribute('href'))
        except NoSuchElementException:
            x = x + 1
    #prints the list
    print("Bing Results:" + str(links))
    searching_ddg()

def searching_ddg():
    # searching for the varialbe "searchup" which contains the input before running the script, on google
    driver.get("https://www.duckduckgo.com")
    time.sleep(2.4)
    searchbox = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[2]/form/input[1]')
    searchbox.send_keys(searchup)
    searchbox.send_keys(Keys.ENTER)
    flnp_dgg()

def flnp_dgg():
    time.sleep(2.4)
    # finding links, putting them in a list and then printing it out
    links = []
    for x in range(1, 6):
        # goes through the results and adds the first 5 links to the list
        try:
            links.append(driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[3]/div/div[1]/div[5]/div[' + str(x) + ']/div/h2/a[1]').get_attribute('href'))
        except NoSuchElementException:
            x = x + 1
    #prints the list
    print("DuckDuckGo Results:" + str(links))
    searching_yandex()

def searching_yandex():
    # searching for the varialbe "searchup" which contains the input before running the script, on google
    driver.get("https://www.yandex.com")
    time.sleep(2.4)
    searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/table/tbody/tr[2]/td[2]/form/div[1]/span/span/input')
    searchbox.send_keys(searchup)
    searchbox.send_keys(Keys.ENTER)
    flnp_yandex()

def flnp_yandex():
    time.sleep(2.4)
    # finding links, putting them in a list and then printing it out
    links = []
    for x in range(1, 6):
        # goes through the results and adds the first 5 links to the list
        try:
            links.append(driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[' + str(x) + ']/div/h2/a').get_attribute('href'))
        except NoSuchElementException:
            x = x + 1
    #prints the list
    print("Yandex Results:" + str(links))
    searching_yahoo()

def searching_yahoo():
    # searching for the varialbe "searchup" which contains the input before running the script, on google
    driver.get("https://www.yahoo.com")
    time.sleep(2.4)
    acceptbox = driver.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/form/button[1]')
    acceptbox.click()
    searchbox = driver.find_element_by_xpath('/html/body/header/div[2]/div/div/div[1]/div[1]/div[1]/div/form/input[1]')
    searchbox.send_keys(searchup)
    searchbox.send_keys(Keys.ENTER)
    flnp_yahoo()

def flnp_yahoo():
    time.sleep(2.4)
    # finding links, putting them in a list and then printing it out
    links = []
    for x in range(1, 6):
        # goes through the results and adds the first 5 links to the list
        try:
            links.append(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[' + str(x) + ']/div/div[1]/h3/a').get_attribute('href'))
        except NoSuchElementException:
            x = x + 1
    #prints the list
    print("Yahoo Results:" + str(links))


# if the user provides an input it will search. this starts the whole sequence. 
if(searchup != None):
    searching_google(searchup)
