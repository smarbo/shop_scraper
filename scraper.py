from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def headless_fetch(url, selector):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    try:
        ep = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        WebDriverWait(driver, 5).until(ep)

        html = driver.page_source

        driver.quit()

        return html

    except Exception as e:
        print(f"An error: {e}")

        driver.quit()
