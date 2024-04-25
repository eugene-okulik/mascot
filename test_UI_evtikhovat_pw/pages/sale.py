from test_UI_evtikhovat_pw.pages.base_page import BasePage
from playwright.sync_api import expect


class Sale(BasePage):
    page_url = '/sale.html'

    def check_20_percent_promo(self):
        promo_title = self.page.locator('a.block-promo.sale-20-off strong.title').text_content()
        promo_info = self.page.locator('a.block-promo.sale-20-off span.info').text_content()
        assert promo_title == '20% OFF'
        assert promo_info == 'Every $200-plus purchase!'

    def woman_deals_redirect(self):
        women_deals_link = self.page.locator("a.block-promo.sale-main").click()

    def check_redirection_to_woman_deals(self):
        expected_url = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
        expect(self.page).to_have_url(expected_url, timeout=5000)

    def header_text_is(self):
        return self.page.locator('h1.page-title#page-title-heading').text_content()

    def check_header_text(self):
        header_locator = self.page.locator('h1.page-title#page-title-heading')
        expected_text = 'Sale'
        expect(header_locator).to_have_text(expected_text)