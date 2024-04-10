from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_product_ordering(driver):
    driver.implicitly_wait(3)
    driver.get('https://www.demoblaze.com/index.html')
    product_link = driver.find_element(By.LINK_TEXT, 'Sony vaio i7')
    ActionChains(driver).key_down(Keys.COMMAND).click(product_link).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-success'))
    )
    add_to_cart_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart_link = driver.find_element(By.LINK_TEXT, 'Cart')
    cart_link.click()
    added_product_name = "Sony vaio i7"
    added_product_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//td[contains(text(), '{added_product_name}')]"))
    )
    added_product_text = added_product_element.text
    assert added_product_text == added_product_name


def test_first_item_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    selector = "img[alt='Push It Messenger Bag']"
    bag = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    add_to_compare = driver.find_element(By.CSS_SELECTOR, '.action.tocompare')
    actions = ActionChains(driver)
    actions.move_to_element(bag)
    actions.click(add_to_compare)
    actions.perform()
    added_item_locator = (
        By.CSS_SELECTOR,
        'a.product-item-link[href="https://magento.softwaretestingboard.com/push-it-messenger-bag.html"]')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(added_item_locator))
    added_item = driver.find_element(*added_item_locator)
    added_item_text = added_item.text
    assert added_item_text == "Push It Messenger Bag"
