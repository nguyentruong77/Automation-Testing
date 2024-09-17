from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

str = input("Nhap vao gia tri can tim: ")
driver.implicitly_wait(5)
cost = driver.find_element(By.NAME, 'q')
cost.send_keys(str)
cost.submit()

results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
for re in results:
    text = re.find_element(By.CSS_SELECTOR, 'a').text
    link = re.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    print(text)
    print(link)
    print("=============================")
driver.close()