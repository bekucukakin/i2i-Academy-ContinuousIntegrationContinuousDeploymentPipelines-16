from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_example_domain_has_correct_title():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    try:
        driver.get("https://example.com")
        assert driver.title == "Example Domain"
    finally:
        driver.quit()