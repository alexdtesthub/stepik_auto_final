import time
from .pages.product_page import ProductPage
import pytest

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     pages = ProductPage(browser, link)
#     pages.open()
#     pages.add_button()
#     pages.solve_quiz_and_get_code()
#     pages.book_path_correct()
#     pages.book_price_correct()

#def test_book_path_correc(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #pages = ProductPage(browser, link)
    #pages.open()
    #pages.book_path_correct()

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# def test_guest_can_add_product_to_basket(browser, link):
#          pages = ProductPage(browser, link)
#          pages.open()
#          pages.add_button()
#          pages.solve_quiz_and_get_code()
#          pages.book_path_correct(link)
#          pages.book_price_correct(link)

#LASTESTS

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
#     pages = ProductPage(browser, link)
#     pages.open()
#     pages.add_button()
#     pages.solve_quiz_and_get_code()
#     pages.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser, link):
#     pages = ProductPage(browser, link)
#     pages.open()
#     pages.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_basket(browser, link):
#     pages = ProductPage(browser, link)
#     pages.open()
#     pages.add_button()
#     pages.solve_quiz_and_get_code()
#     pages.should_not_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    pages = ProductPage(browser, link)
    pages.open()
    pages.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    pages = ProductPage(browser, link)
    pages.open()
