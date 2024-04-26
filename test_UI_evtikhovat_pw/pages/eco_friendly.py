from test_UI_evtikhovat_pw.pages.base_page import BasePage
from playwright.sync_api import expect


class EcoFriendlySorting(BasePage):
    page_url = '/collections/eco-friendly.html'

    def sort_items_by_name_descending(self):
        self.page.locator('#sorter').first.select_option('Product Name')
        descending_order = self.page.get_by_text('Set Descending Direction').first
        descending_order.hover()
        descending_order.click()
        self.page.wait_for_timeout(3000)
        ascending_order = self.page.get_by_text('Set Ascending Direction').first
        expect(ascending_order).to_have_text('Set Ascending Direction')

    def check_first_item_after_sorting_descending(self):
        first_item_locator = self.page.get_by_text('Tiffany Fitness Tee')
        expect(first_item_locator).to_have_text('Tiffany Fitness Tee')

    def sort_items_by_price(self):
        self.page.locator('#sorter').first.select_option('Price')

    def check_first_item_after_sorting(self):
        first_item_locator = self.page.get_by_text("Atlas Fitness Tank")
        expect(first_item_locator).to_have_text('Atlas Fitness Tank')

    def check_initial_toolbar_text(self):
        toolbar_text_locator = self.page.locator('#toolbar-amount').nth(0)
        toolbar_text_locator.text_content()
        expect(toolbar_text_locator).to_have_text("Items 1-12 of 18")

    def switch_to_list_view(self):
        self.page.locator('#mode-list').nth(0).click()

    def check_updated_toolbar_text(self):
        toolbar_text_locator = self.page.locator('#toolbar-amount').nth(0)
        toolbar_text_locator.text_content()
        expect(toolbar_text_locator).to_have_text("Items 1-10 of 18")
