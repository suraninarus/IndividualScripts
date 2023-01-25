from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class DownLoader:
    pass


chrome_driver = r"C:\Drivers\Chrome\chromedriver.exe"   # Driver on the office machine
url_path = r"https://www.dijnet.hu/"
user = "hozsolti"
passwd = "Forzaarsenal96"

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url_path)
driver.maximize_window()

# creating the wait
wait = WebDriverWait(driver, 30)

# click the logon button
login_button = wait.until(EC.visibility_of(driver.find_element(By.ID, "login-btn")))
login_button.click()

# fill in the username and pass word
username_field = wait.until(EC.visibility_of(driver.find_element(By.NAME, "username")))
username_field.send_keys(user)
pwd_field = wait.until(EC.visibility_of(driver.find_element(By.NAME, "password")))
pwd_field.send_keys(passwd)
pwd_field.send_keys(Keys.ENTER)

bills_button = wait.until(EC.visibility_of(driver.find_element(By.XPATH, '//*[@id="logged_menu"]/li[3]/a')))
bills_button.click()

cookie = wait.until(EC.visibility_of(driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")))
cookie.click()

select_text = driver.find_elements(By.NAME, "szlaszolgnev")
dropdown_options_list = select_text[0].text.split('\n')


# Így megtalálja a dropdown-ban a különböző szolgáltató neveket
# a = driver.find_element(By.XPATH, '//*[@id="sopts"]//option[2]'.format())
# a.click()

# driver.close()


