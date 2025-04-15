import allure
import pytest
import logging
import tempfile
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

@pytest.fixture
def driver():
    # Настройка ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # без графического интерфейса
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

@pytest.fixture(scope="function")
def driver(request):
    # Настройка логгера
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)
    
    # Конфигурация ChromeOptions
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # Уникальный user-data-dir для каждого теста
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    
    # Инициализация драйвера
    driver = webdriver.Chrome(options=options)
    logger.info("Браузер запущен")
    
    yield driver
    
    # Завершение
    driver.quit()
    logger.info("Браузер закрыт")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
