import pytest
from main_page import MainPage


def test_register_and_add_to_wishlist(driver, fake):
    # Генерация данных
    user_data = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "email": fake.email(),
        "password": "123456"
    }

    # 1. Открываем главную страницу
    main_page = MainPage(driver)
    main_page.driver.get("https://demo.opencart.com/")

    # 2. Регистрация
    register_page = main_page.open_account_menu().click_register()
    main_page = register_page.register_user(**user_data)

    # 3. Добавление в вишлист
    product_page = main_page.open_first_product()
    product_page.add_to_wishlist()

    # Проверка успешного добавления
    assert "Success" in product_page.get_alert_text()