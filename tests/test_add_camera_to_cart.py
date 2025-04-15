import pytest
from main_page import MainPage


def test_add_camera_to_cart(driver):
    # 1. Открываем главную страницу
    main_page = MainPage(driver)
    
