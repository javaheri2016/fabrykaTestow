from selenium import webdriver
from helpers.helpers import scrolling_to_element

driver = webdriver.Chrome('/Users/katarzynajavaheri/PycharmProjects/tapsGitProject/chromedriver')

driver.get('https://fabrykatestow.pl')
link = driver.find_element_by_link_text('KURS TAPS')
link.click()
scrolling_to_element(driver, '//*[@id="content"]/div/div/div/div/div/div/div/section[9]/div[2]/div/div/div/div/section/div/div/div[1]/div/div/div[1]/div/div/img')
driver.get_screenshot_as_file("screenshot.png")
driver.quit()

