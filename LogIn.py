import time

def logIn(driver):

    accounts = open("ACCOUNT.txt")
    content = accounts.readlines()

    driver.get("https://www.instagram.com/direct/inbox/")

    driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()

    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label').send_keys(content[0])
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label').send_keys(content[1])
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
