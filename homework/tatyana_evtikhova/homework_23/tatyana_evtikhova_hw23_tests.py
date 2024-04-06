import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver


def test_single_select(driver):
    expected_result = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_element = driver.find_element(By.ID, 'id_choose_language')
    select = Select(select_element)
    select.select_by_visible_text('Python')
    driver.find_element(By.ID, 'submit-id-submit').click()
    result_text_element = driver.find_element(By.ID, 'result-text')
    result_text = result_text_element.text
    assert result_text == expected_result


def test_dynamic_loading(driver):
    expected_result = "Hello World!"
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.CSS_SELECTOR, '#start button')
    start_button.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish h4')))
    hello_world_element = driver.find_element(By.CSS_SELECTOR, '#finish h4')
    hello_world_text = hello_world_element.text
    assert hello_world_text == expected_result
