# imports here
from selenium import webdriver
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
        # goes through the results and adds the first 5 links to the list
        if(x != 2):
            links.append(driver.find_element_by_xpath('//*[@id="rso"]/div['+ str(x) +']/div/div[1]/a').get_attribute('href'))
        else:
            x = x + 1
    #prints the list
    print("Google Results:" + str(links))
    print("Thanks for trying out the program! i will be pushing updates like bing, duckduckgo and yandex support tomorrow. that task is for tomorrow me i guess! script by kamalyaka")
# if the user provides an input it will search. this starts the whole sequence. 
if(searchup != None):
    searching_google(searchup)
