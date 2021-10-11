from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/python/example-code-using-selenium-webdriver-python')

assert 'Selenium Easy' in chrome_browser.title
#use CSS selectors
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
user_message.clear()
user_message.send_keys('I am extra cool!')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I am extra cool!' in output_message.text

chrome_browser.close()
#or
#chrome_browser.quit() to close all the sessions



