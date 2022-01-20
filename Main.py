from selenium import webdriver
import pathlib

from LogIn import *
from MessageSender import *

path=str(pathlib.Path(__file__).parent.absolute())
driver = webdriver.Chrome(path+'/chromedriver')

logIn(driver)
messageSender(driver)

driver.quit()

print("")
print("")
print("")
print("[PSUCCESSFULLY COMPLETED PROCESS]")
print("")
print("")
print("")
