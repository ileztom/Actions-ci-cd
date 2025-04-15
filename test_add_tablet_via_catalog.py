import pytest
from main_page import MainPage


def test_add_tablet_via_catalog(driver):
    # 1. Открываем главную страницу
    main_page = MainPage(driver)
    main_page.driver.get("https://demo.opencart.com/")

    # 2. Открываем каталог планшетов
    main_page.open_tablets_catalog()

    # 3. Открываем первый планшет в списке
    product_page = main_page.open_first_tablet()

    # 4. Добавляем в корзину
    product_page.add_to_cart()

    # 5. Проверяем успешность добавления
    assert "Success" in product_page.get_alert_text()
    assert "Samsung Galaxy Tab 10.1" in product_page.get_alert_text()