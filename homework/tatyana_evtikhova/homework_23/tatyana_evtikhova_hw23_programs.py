from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()

input_data = "automated_testing_123"
chrome_driver.get('https://www.qa-practice.com/elements/input/simple')
text_string = chrome_driver.find_element(By.NAME, 'text_string')
text_string.send_keys(input_data)
text_string.send_keys(Keys.ENTER)
result_text = chrome_driver.find_element(By.ID, 'result-text')
print(result_text.text)

chrome_driver.get('https://demoqa.com/automation-practice-form')
chrome_driver.find_element(By.ID, 'firstName').send_keys('TE')
chrome_driver.find_element(By.ID, 'lastName').send_keys('user1')
chrome_driver.find_element(By.ID, 'userEmail').send_keys('TEuser1@test.comx')
chrome_driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-2"]').click()
chrome_driver.find_element(By.ID, 'userNumber').send_keys(4812345678)
element = chrome_driver.find_element(By.ID, 'dateOfBirthInput')
chrome_driver.execute_script("arguments[0].scrollIntoView(true);", element)
element = WebDriverWait(chrome_driver, 10).until(EC.element_to_be_clickable((By.ID, 'dateOfBirthInput')))
element.click()
Select(chrome_driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')).select_by_visible_text('July')
Select(chrome_driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')).select_by_visible_text('1996')
date_elements = chrome_driver.find_elements(By.CSS_SELECTOR, '.react-datepicker__day')
for date_element in date_elements:
    if date_element.text == '20':
        date_element.click()
        break
chrome_driver.find_element(By.ID, 'subjectsInput').send_keys('test subject')
chrome_driver.find_element(By.CSS_SELECTOR, '[for="hobbies-checkbox-3"]').click()
chrome_driver.find_element(By.ID, 'currentAddress').send_keys('1st Main Street')
state_element = chrome_driver.find_element(By.ID, 'state')
state_element.click()
haryana_option = chrome_driver.find_element(By.XPATH, '//div[@id="state"]//div[text()="Haryana"]')
haryana_option.click()
city_element = chrome_driver.find_element(By.ID, 'city')
city_element.click()
karnal_option = chrome_driver.find_element(By.XPATH, '//div[@id="city"]//div[text()="Karnal"]')
karnal_option.click()

chrome_driver.find_element(By.ID, 'submit').click()

modal_body = chrome_driver.find_element(By.CLASS_NAME, "modal-body")
table = modal_body.find_element(By.TAG_NAME, "table")
rows = table.find_elements(By.TAG_NAME, "tr")
data = {}
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) == 2:
        label = cells[0].text
        value = cells[1].text
        data[label] = value
for label, value in data.items():
    print(f"{label}: {value}")
