from selenium import webdriver

import time

#commands: driver.quit  driver.close  driver.title  driver.page_source  .send_keys("")

book = input(str('Please type the exact name of the book you are looking for to see if it is available at our library'))

PATH = r"/Users/juanberasateguigallego/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://tilburguniversity.on.worldcat.org/discovery")

searchbox = driver.find_element_by_id("query")
searchbox.click()
searchbox.clear()
searchbox.send_keys(book)

searchbutton = driver.find_element_by_id("headersubmit")
searchbutton.click()

continue_auth = driver.find_element_by_id("continue-as-guest")
continue_auth.click()


title_book1 = driver.find_element_by_css_selector("[aria-controls^='action_panel_1']")
title_book1.click()

time.sleep(1.5)
availability = driver.find_element_by_class_name('availability_level_total')

print(availability.text)
