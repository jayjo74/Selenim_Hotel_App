import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    print("Running class level setUp")
    url = "http://adactin.com/HotelApp/index.php"
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    # driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    # if request.cls is not None:
    #     request.cls.driver = driver
    # yield driver
    yield
    # driver.close()
    driver.quit()
    print("Running class level tearDown")

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")