import pytest
from main_page import MainPage


def test_add_camera_to_cart(driver):
    # 1. Открываем главную страницу
    main_page = MainPage(driver)
    main_page.driver.get("https://demo.opencart.com/")

    # 2. Открываем страницу камеры
    product_page = main_page.open_camera_product()

    # 3. Добавляем в корзину
    product_page.add_to_cart()

    # 4. Проверяем успешность добавления
    assert "Success" in product_page.get_alert_text()
    assert "Canon EOS 5D" in product_page.get_alert_text()