# simple web scraper via xpath
from selenium import webdriver
import time 


url = 'https://www.youtube.com/channel/UCFTM1FGjZSkoSPDZgtbp7hA'
path_to_chromedriver = './chromedriver'  # change as necessary

browser = webdriver.Chrome(path_to_chromedriver)
browser.get(url)

time.sleep(3)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
browser.quit()
