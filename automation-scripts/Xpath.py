from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.automationtesting.in/Register.html")

#Xpath syntax
#//tagname[@attribute = 'value']
#//*[@attribute = 'value']
//input[@placeholder = "First Name"]
#OR
//*[@placeholder = "First Name"]

#Xpath to find full text
//label[text() ="Full Name* " ]

#Xpath to find partial text
//label[contains(text(),'Full Name')]

#to find inddex
//label[2]
//input[2]

#Xpath with operators
//*[@placeholder="First Name" and @ng-model="FirstName"]
//*[@placeholder="First Name" or @ng-model="FirstName"]

#to get child method
//form[@id="basicBootstrapForm"]//child::div

#to find parent
//form@id="basicBootstrapForm"]/parent::div

##to find ancestor
//form[@id="basicBootstrapForm"]/ancestor::div

#following- sibling - preceding
//input[@id='checkbox1']//following-sibling::label
//input[@id='checkbox1']//preceding-sibling::label