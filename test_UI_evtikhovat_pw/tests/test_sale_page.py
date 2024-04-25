import pytest


def test_20_percent_promo(sale_page):
    sale_page.open_page()
    sale_page.check_20_percent_promo()


def test_women_deals_page(sale_page):
    sale_page.open_page()
    sale_page.woman_deals_redirect()
    sale_page.check_redirection_to_woman_deals()


def test_sale_header(sale_page):
    sale_page.open_page()
    sale_page.check_header_text()
