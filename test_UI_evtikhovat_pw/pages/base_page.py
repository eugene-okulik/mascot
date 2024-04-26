from playwright.sync_api import Page


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
            consent_button = self.page.locator('p.fc-button-label:text("Consent")')
            consent_button.click()
        else:
            raise NotImplementedError('Page can not be opened for this page class')
