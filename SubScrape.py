from selenium import webdriver
from time import * #I don't have to write 'time.' everytime
from selenium.webdriver.common.keys import Keys


def run():
    chrome_path = r"" #Put the path to your chromedriver here
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://www.youtube.com/feed/subscriptions")

    user = "" #input your own user and pass
    password = ""

    sleep(2) #this is so the page has time to load
    driver.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(user)
    driver.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(Keys.RETURN)
    sleep(2)
    driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(password)
    driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(Keys.RETURN)
    sleep(2)

    #Systematically tries to find each video capsule and then put the video title and creator into a list
    #called subs. Only puts the first 9 videos into the list
    count = 0
    Subs = []
    for vid in driver.find_elements_by_xpath("""//*[@id="dismissable"]"""):
        count += 1
        if count >= 10:
            break
        title = vid.find_element_by_xpath('.//*[@id="video-title"]').text
        creator = vid.find_element_by_xpath('.//*[@id="byline"]/a').text

        Subs.append({'title': title, 'creator': creator})

    '''print(Subs) used for debugging'''

    file_l = open("listSUB.txt", "w+") #Outputs the list to a file
    skip1 = 0
    for video in Subs:
        if skip1 != 0:
            file_l.write("%s\n" %video)
        skip1 += 1


if __name__ == "__main__":
    run();