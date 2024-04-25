def test_successful_registration(login_page):
    login_page.open_page()
    login_page.fill_registration_form("Test", "User", "Test1234", "Test1234")
    login_page.check_successful_registration()


def test_guest_post_message(login_page):
    login_page.open_page()
    login_page.check_guest_message()


def test_email_validation(login_page):
    login_page.open_page()
    login_page.invalid_email()
    login_page.check_email_validation()
