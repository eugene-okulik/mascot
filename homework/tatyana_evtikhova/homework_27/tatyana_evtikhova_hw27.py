from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert_ok(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result = new_page.locator('#result')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    page.locator('#new-page-button').is_enabled()


def test_colour_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button_text_element = page.locator('#colorChange')
    expected_rgb_color = 'rgb(220, 53, 69)'
    expect(button_text_element).to_have_css('color', expected_rgb_color)
    page.click('#colorChange')
