import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


twitter_username = "RNTata2000"
browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
browser.get("https://twitter.com/" + twitter_username)

time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 5

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

twitter_elm = browser.find_elements_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
#print twitter_elm

for post in twitter_elm:
    username = post.find_elements_by_class_name("username")
    print(username.txt)
    if username.text.lower() == "@" + twitter_username.lower():
        tweet = post.find_element_by_class_name("tweet-text")
        print(tweet.text)

browser.quit()