from selenium import webdriver
from helpers.helpers import scrolling_to_element
import time

driver = webdriver.Chrome('/Users/katarzynajavaheri/PycharmProjects/tapsGitProject/chromedriver')

driver.get('https://javaheri.pl')
link = driver.find_element_by_link_text('KONTAKT')
link.click()
scrolling_to_element(driver, '//*[@id="post-23"]/div[2]/div/div/div/div/section[3]/div/div/div/div/div/div[4]/div/div/div')
time.sleep(3)
driver.get_screenshot_as_file("screenshot.png")
driver.quit()

