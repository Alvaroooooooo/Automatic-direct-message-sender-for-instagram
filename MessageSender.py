import time

def messageSender(driver):
    time.sleep(4)
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

    users = open("USERS.txt")
    content = users.readlines()

    message = open("MESSAGE.txt")
    message2 = message.readline()

    for i in range(len(content)):
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(content[i])
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message2)
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
        print("Message '"+message2+"' successfully sent to "+content[i])

        time.sleep(2)
