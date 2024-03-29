import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_file(browser: str, files_dir: str, report_url: str, login: str, password: str):
    if browser == 'Edge':
        options = EdgeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": files_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": "false",
            "plugins.always_open_pdf_externally": True
            }
        )
        driver = webdriver.Edge(options=options)
    elif browser == 'Chrome':
        options = ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": files_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": "false",
            "plugins.always_open_pdf_externally": True
            }
        )
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Driver {browser} not supported.")


    driver.maximize_window()
    driver.get(report_url)

    driver.find_element(By.XPATH, '//*[@id="j_username"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="j_password_pseudo"]').send_keys(password)

    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]'))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="apply"]'))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ok"]'))).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export"]'))).click()

    driver.find_elements(By.CSS_SELECTOR, "[id*=menuList_simpleAction]")[0].click()
    time.sleep(2)


