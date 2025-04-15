import pytest
from main_page import MainPage


def test_write_tablet_review(driver):
    # 1. Открываем главную страницу
    main_page = MainPage(driver)
    main_page.driver.get("https://demo.opencart.com/")

    # 2. Открываем каталог планшетов
    main_page.open_tablets_catalog()

    # 3. Открываем первый планшет в списке
    product_page = main_page.open_first_tablet()

    # 4. Переходим на вкладку Reviews
    product_page.open_reviews_tab()

    # 5. Заполняем и отправляем отзыв
    product_page.submit_review(
        name="Test User",
        text="Very good, chetko"
    )

    # 6. Проверяем успешность отправки
    assert product_page.is_review_submitted()