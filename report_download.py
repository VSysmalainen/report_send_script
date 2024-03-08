from main_env import login, password, browser
import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import EdgeOptions, ChromeOptions


download_dir = os.path.dirname(os.path.abspath(__file__)) + '\\files'


def download_file():
    if browser == 'Edge':
        options = EdgeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": "false",
            "plugins.always_open_pdf_externally": True
            }
        )
        driver = webdriver.Edge(options=options)
    elif browser == 'Chrome':
        options = ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": "false",
            "plugins.always_open_pdf_externally": True
            }
        )
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Driver {browser} not supported.")


    driver.maximize_window()

    driver.get("http://report.rzd.internal:8080/")

    user_id_button = driver.find_element(By.XPATH, "/html/body[@id='loginPage']/div[@id='frame']/div[@class='content']/div[@id='display']/div[@class='wrapper']/form[@id='loginForm']/div[@id='login']/div[@class='content hasFooter ']/div[@class='body  ']/div[@class='inputSection']/fieldset[1]/input[@id='j_username']")
    user_id_button.send_keys(login)

    pass_button = driver.find_element(By.XPATH, "/html/body[@id='loginPage']/div[@id='frame']/div[@class='content']/div[@id='display']/div[@class='wrapper']/form[@id='loginForm']/div[@id='login']/div[@class='content hasFooter ']/div[@class='body  ']/div[@class='inputSection']/fieldset[1]/input[@id='j_password_pseudo']")
    pass_button.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element(By.XPATH, "/html/body[@id='loginPage']/div[@id='frame']/div[@class='content']/div[@id='display']/div[@class='wrapper']/form[@id='loginForm']/div[@id='login']/div[@class='content hasFooter ']/div[@class='footer ']/div[@class='inputSection']/button[@id='submitButton']/span[@class='wrap']")
    login_button.click()
    time.sleep(5)

    driver.get("http://report.rzd.internal:8080/jasperserver/flow.html?_flowId=viewReportFlow&_flowId=viewReportFlow&ParentFolderUri=%2FReports%2FCase&reportUnit=%2FReports%2FCase%2FDaily&standAlone=true")
    time.sleep(5)

    apply_button = driver.find_element(By.XPATH, '//*[@id="apply"]')
    apply_button.click()
    time.sleep(2)

    ok_button = driver.find_element(By.XPATH, '//*[@id="ok"]')
    ok_button.click()
    time.sleep(2)

    menu_icon = driver.find_element(By.XPATH, '//*[@id="export"]')
    menu_icon.click()
    time.sleep(1)

    menu_list = driver.find_elements(By.CSS_SELECTOR, "[id*=menuList_simpleAction]")
    menu_list[0].click()
    time.sleep(2)
