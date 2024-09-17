import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://www.thegioididong.com/')
driver.maximize_window()
driver.find_element(By.XPATH, '/html/body/header/div[2]/div/ul/li[1]').click()


Phones = driver.find_elements(By.CSS_SELECTOR, 'li.ajaxed')
with open('Phones.csv', 'w', newline = '', encoding = 'utf-8') as f:
    fieldName = ['Name', 'Price']
    writer = csv.DictWriter(f, fieldnames = fieldName)
    writer.writeheader()
    for ip in Phones:
        try:
            name = ip.find_element(By.TAG_NAME, 'h3').text
            price = ip.find_element(By.TAG_NAME, 'strong').text
            writer.writerow({'Name': name, 'Price': price})
            print(name)
            print(price)
            print('======================')
        except NoSuchElementException:
            print("Loi")
driver.close()

