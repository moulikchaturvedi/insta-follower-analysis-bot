from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import time
from collections import Counter

file_path = 'C:/CustomPrograms/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(file_path)
# driver = webdriver.Chrome() if your chromedriver.exe inside root


# hard-coded to check for a particular ID
instagram_url = "http://www.instagram.com/<username>"
instagram_username = "<username>"
instagram_password = "<password>"

driver.get("http://www.instagram.com/")

# Enters the username and password
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
username.send_keys(instagram_username)
password.clear()
password.send_keys(instagram_password)
Login_button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# Handles Pop Ups
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


# Checks my following list and stores them in a list and writes them to a txt file

#Opens following list
driver.get(instagram_url)
following_open = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(., "following")]'))).click()

#for a normal following list(200-250) for general purposes
# page_down_iteration = 25
# for page_down in range(page_down_iteration):
#     time.sleep(3)
#     scrollable_div = driver.find_element_by_xpath('//div[@class="isgrP"]')
#     scrollable_div.click()
#     ActionChains(driver).send_keys(Keys.END).perform()


#for a very short following list for test purposes
time.sleep(2)
scrollable_div = driver.find_element_by_xpath('//div[@class="isgrP"]')
scrollable_div.click()
ActionChains(driver).send_keys(Keys.END).perform()

#appends all following to a python list
following = driver.find_elements_by_xpath(
    '//span/a[@class="FPmhX notranslate  _0imsa "]')
following_list = []
for p in range(len(following)):
    following_list.append(following[p].text)
    print(p)

#writes all following to a txt file
textfile = open("following.txt", "w")
for element in following_list:
    textfile.write(element + "\n")
textfile.close()


# Checks my followers list and stores them in a list and writes them to a txt file

#Opens followers list
driver.get(instagram_url)
following_open = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(., "followers")]'))).click()

#for a normal followers list(200-250) for general purposes
# page_down_iteration = 25
# for page_down in range(page_down_iteration):
#     time.sleep(3)
#     scrollable_div = driver.find_element_by_xpath('//div[@class="isgrP"]')
#     scrollable_div.click()
#     ActionChains(driver).send_keys(Keys.END).perform()


#for a very short followers list for test purposes
time.sleep(2)
scrollable_div = driver.find_element_by_xpath('//div[@class="isgrP"]')
scrollable_div.click()
ActionChains(driver).send_keys(Keys.END).perform()

#appends all followers to a python list
followers = driver.find_elements_by_xpath(
    '//span/a[@class="FPmhX notranslate  _0imsa "]')
followers_list = []
for p in range(len(followers)):
    followers_list.append(followers[p].text)
    print(p)

#writes all followers to a txt file
textfile = open("followers.txt", "w")
for follower in followers_list:
    textfile.write(follower + "\n")
textfile.close()


# Checking people who don't follow back

# Checks who doesn't follow back by subtracting my followers from people I follow
not_following_back = Counter(following_list) - Counter(followers_list)
list(not_following_back.elements())

# writes the names of the people who don't follow back to a txt file
textfile = open("not_following_back.txt", "w")
for unfollower in not_following_back:
    textfile.write(unfollower + "\n")
textfile.close()
