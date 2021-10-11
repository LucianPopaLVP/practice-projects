from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/python/example-code-using-selenium-webdriver-python')

print('Selenium Easy' in chrome_browser.title)