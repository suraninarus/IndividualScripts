"""
PSEUDOCODE:

get login_name
set driver path

instantiate the driver_1
create wait
got to webpage
logon
cookie ok
find "Számlakeresés" + click
get provider name list
close driver_1
loop trough provider_name_list and call "Class Driver" on each

    Class driver:
        init(driver, provider_name)
            set ChormeDownload options
            instantiate the driver_X
            create wait
            call Class 2
            close driver_X

        set_download_dir()
            set download directory
            (if download directory does not exist create directory)

        logon()
            got to webpage
            logon
            cookie ok

        provider_page()
            find "Számlakeresés" + click
            find provider_name + click

        number_of_rows()
            get number of rows

    meth downloader(number of rows, ):
        choose a row and + click (var row +=1)
        find the "Letöltés" + click
        find "Számla nyomtatható verziója (PDF) - Hiteles számla" + click
        while not all rows were clicked call the Class3 recursivelly
            goback to the row page choose the next row
"""
import configparser
from os import getlogin
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ini_path = r'C:\Users\A87484215\PycharmProjects\IndividualScripts\billingProvider.ini'
url_path = r"https://www.dijnet.hu/"


def get_info(ini_path, section, key):
    """ needed because the chromedriver has different paths on different machines """
    config = configparser.ConfigParser()
    config.read(ini_path)
    Key = config[section]
    value = Key[key]
    return value

def initial_driver(url, path, user, passwd):
    """gets the provider list"""
    driver = webdriver.Chrome(path)
    wait = WebDriverWait(driver, 30)
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    driver.maximize_window()
    login_button = wait.until(EC.visibility_of(driver.find_element(By.ID, "login-btn")))
    login_button.click()
    username_field = wait.until(EC.visibility_of(driver.find_element(By.NAME, "username")))
    username_field.send_keys(user)
    pwd_field = wait.until(EC.visibility_of(driver.find_element(By.NAME, "password")))
    pwd_field.send_keys(passwd)
    pwd_field.send_keys(Keys.ENTER)
    cookie = wait.until(
        EC.visibility_of(driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")))
    cookie.click()
    # sleep(5)                # FUUUUUUUUUUUUUUUUUUCK
    wait.until(EC.visibility_of(driver.find_element(By.XPATH, '//*[@id="logged_menu"]/li[3]/a')))
    bills_button = driver.find_element(By.XPATH, '//*[@id="logged_menu"]/li[3]/a')
    # bills_button = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="logged_menu"]/li[3]/a')))
    bills_button.click()
    select_text = driver.find_elements(By.NAME, "szlaszolgnev")
    provider_dropdown_options_list = select_text[0].text.split('\n')
    # driver.close()
    return provider_dropdown_options_list

"""
loop trough provider_name_list and call "Class Driver" on each
"""

"""get login_name / set driver path"""
user = getlogin()
driver_path = get_info(ini_path, 'chromeDriver', user)
login_user = get_info(ini_path, 'userInfo', "user")
login_passwd = get_info(ini_path, 'userInfo', "passwd")


provider_list = initial_driver(url_path, driver_path, login_user, login_passwd)
print(provider_list)

for provider in provider_list:
    """call calsses"""
    pass