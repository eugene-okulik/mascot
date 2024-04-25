from playwright.sync_api import BrowserContext
import pytest
from test_UI_evtikhovat_pw.pages.sale import Sale
from test_UI_evtikhovat_pw.pages.eco_friendly import EcoFriendlySorting
from test_UI_evtikhovat_pw.pages.create_account import AccountCreation


@pytest.fixture()
def sale_page(page):
    return Sale(page)


@pytest.fixture()
def login_page(page):
    return AccountCreation(page)


@pytest.fixture()
def ecofriendly_page(page):
    return EcoFriendlySorting(page)


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    # page.set_viewport_size({'width': 1920, 'height': 1080})
    return page
