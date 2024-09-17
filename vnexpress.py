from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

driver = webdriver.Chrome()
driver.get('https://vnexpress.net/')
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="wrap-main-nav"]/nav/ul/li[10]/a').click()
print('Tieu de trang web: ', driver.title)

baibao = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
for info in baibao:
    try:
        tieude = info.find_element(By.CSS_SELECTOR, 'h3 > a').text
        mota = info.find_element(By.CSS_SELECTOR, 'p.description').text
        link = info.find_element(By.CSS_SELECTOR, 'h3 > a').get_attribute('href')
        print('Tieu de: ', tieude, '\n', 'Mo ta: ', mota, '\n', 'Link: ', link,
              '\n', '-----------------------------------------')
    except NoSuchElementException:
        print('Khong the lay')

#Cau 2
with open('News.csv', 'w', newline = '', encoding = 'UTF-8') as f:
    fieldName = ['Title', 'Decsription', 'Link']
    write = csv.DictWriter(f, fieldnames = fieldName)
    write.writeheader()
    baibao1 = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')
    for info in baibao1:
        try:
            tieude = info.find_element(By.CSS_SELECTOR, 'h3 > a').text
            mota = info.find_element(By.CSS_SELECTOR, 'p.description').text
            link = info.find_element(By.CSS_SELECTOR, 'h3 > a').get_attribute('href')
            write.writerow({'Title': tieude, 'Decsription': mota, 'Link': link})
        except NoSuchElementException:
            print('Khong the lay thong tin')
f.close()
driver.close()