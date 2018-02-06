from selenium import webdriver
from time import * # so that I don't have to write 'time.' everytime
from selenium.webdriver.common.keys import Keys


def run():
    chrome_path = r"" # Put the path to your chromedriver here, inorder to instantiate selenium's ability to interact with Chrome
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://www.youtube.com/feed/subscriptions") # the website I am trying to go to

    user = "" # input your own username and password
    password = ""

    sleep(2) # this is so the page has time to load
    # Fill in username
    driver.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(user)
    driver.find_element_by_xpath("""//*[@id="identifierId"]""").send_keys(Keys.RETURN)
    sleep(2)
    # Fill in password
    driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(password)
    driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(Keys.RETURN)
    sleep(2)

    # Systematically tries to find each video capsule and then put the video title and creator into a list
    # called subs. Only puts the first 9 videos into the list
    count = 0
    Subs = []
    # Searched through the larger container dismissables
    for vid in driver.find_elements_by_xpath("""//*[@id="dismissable"]"""):
        count += 1
        if count >= 10:
            break
        title = vid.find_element_by_xpath('.//*[@id="video-title"]').text
        creator = vid.find_element_by_xpath('.//*[@id="byline"]/a').text

        Subs.append({'title': title, 'creator': creator})

    '''print(Subs) used for debugging'''

    file_l = open("listSUB.txt", "w+") # Outputs the list to a file
    skip1 = 0
    for video in Subs:
        if skip1 != 0: # Quick solution to it printing out the first video twice: Need to figure out why.
            file_l.write("%s\n" %video)
        skip1 += 1


if __name__ == "__main__":
    run();
