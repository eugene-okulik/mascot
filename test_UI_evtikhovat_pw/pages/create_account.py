from test_UI_evtikhovat_pw.pages.base_page import BasePage
from playwright.sync_api import expect
from playwright.sync_api import Page
import random
import string


class AccountCreation(BasePage):
    page_url = '/customer/account/create/'

    def fill_registration_form(self, firstname, lastname, password, confirmation_password):
        email = self.generate_random_email()
        firstname_field = self.page.locator("#firstname").fill(firstname)
        lastname_field = self.page.locator("#lastname").fill(lastname)
        email_field = self.page.locator("#email_address").fill(email)
        password_field = self.page.locator("#password").fill(password)
        confirmation_password_field = self.page.locator("#password-confirmation").fill(
            confirmation_password)
        button = self.page.locator('.action.submit.primary').click()

    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
        return f"{random_string}@example.com"

    def check_successful_registration(self):
        message_element = self.page.locator('//div[contains(text(), "Thank you for registering with '
                                            'Main Website Store.")]')
        expect(message_element).to_have_text('Thank you for registering with Main Website Store.')

    def check_guest_message(self):
        message_element = self.page.locator("[id=\"store\\.links\"]").get_by_text("Click “Write for us” link in")
        expect(message_element).to_have_text('Click “Write for us” link in the footer to submit a guest post')

    def invalid_email(self):
        email_input = self.page.locator("#email_address").fill('invalid email')
        submit_button = self.page.locator('[title="Create an Account"]').click()

    def check_email_validation(self):
        error_locator = self.page.locator('#email_address-error')
        expect(error_locator).to_have_text('Please enter a valid email address (Ex: johndoe@domain.com).')
