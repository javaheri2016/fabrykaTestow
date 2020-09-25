from homeworks.simple_test_site.tests.helpers.support_functions import *
from selenium.webdriver import ActionChains


drag_tab = 'draganddrop-header'
drag_content = 'draganddrop-content'
first_column = 'column-a'
second_column = 'column-b'
first_column_text = '//*[@id="column-a"]/header'
second_column_text = '//*[@id="column-b"]/header'


def click_drag_and_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_tab)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_content)
    return elem.is_displayed()


def check_pristine_state(driver_instance):
    text1 = driver_instance.find_element_by_xpath(first_column_text).text
    text2 = driver_instance.find_element_by_xpath(second_column_text).text
    if text1 == 'A' and text2 == 'B':
        return True
    else:
        return False


def check_changed_state(driver_instance):
    square1 = driver_instance.find_element_by_id(first_column)
    square2 = driver_instance.find_element_by_id(second_column)
    text1 = driver_instance.find_element_by_xpath(first_column_text).text
    text2 = driver_instance.find_element_by_xpath(second_column_text).text
    ActionChains(driver_instance).drag_and_drop(square1, square2)
    if text1 == 'B' and text2 == 'A':
        return True
    else:
        return False