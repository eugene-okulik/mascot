from playwright.sync_api import Page, Request, Route, APIResponse
import json


def test_check_response(page: Page):
    def change_response(route):
        with open('digitalmat.json', 'r') as file:
            data = json.load(file)
        body = json.dumps(data)
        route.fulfill(body=body)
    page.route("https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat",
               change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone15pro = page.locator('.rf-hcard-content-title:has-text("iPhone 15 Pro")')
    iphone15pro.click()
    header_locator = page.locator('h2.rf-digitalmat-overlay-header.typography-manifesto#rf-digitalmat-overlay-label-0'
                                  ':has-text("яблокофон 15 про")')
    header_text = header_locator.text_content()
    assert header_text.strip() == "яблокофон 15 про"
