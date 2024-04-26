import pytest


@pytest.mark.extended
def test_descending_order(ecofriendly_page):
    ecofriendly_page.open_page()
    ecofriendly_page.sort_items_by_name_descending()
    ecofriendly_page.check_first_item_after_sorting_descending()


@pytest.mark.extended
def test_sorting(ecofriendly_page):
    ecofriendly_page.open_page()
    ecofriendly_page.sort_items_by_price()
    ecofriendly_page.check_first_item_after_sorting()


@pytest.mark.smoke
def test_switch_view(ecofriendly_page):
    ecofriendly_page.open_page()
    ecofriendly_page.check_initial_toolbar_text()
    ecofriendly_page.switch_to_list_view()
    ecofriendly_page.check_updated_toolbar_text()
