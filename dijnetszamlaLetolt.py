from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# path = r"C:\Users\Zsolt\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\names.txt"
chrome_driver = r"C:\Users\Zsolt\Desktop\learningMaterial\Python\Selenium\drivers\chromedriver_win32\chromedriver.exe"
url_path = r"https://www.dijnet.hu/"
user = "hozsolti"
passwd = "Forzaarsenal96"


# got to the homepage
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
driver.get(url_path)

# login
login_button = driver.find_element(By.ID, "login-btn")   # HERE I NEED A WAIT
login_button.click()
username_field = driver.find_element(By.NAME, "username") # HERE I NEED A WAIT
username_field.send_keys(user)
username_field = driver.find_element(By.NAME, "password")
username_field.send_keys(passwd)
username_field.send_keys(Keys.ENTER)



# find the billing surface: //*[@id="logged_menu"]/li[3]/a
search_bill_button = driver.find_element(By.XPATH, '//*[@id="logged_menu"]/li[3]/a')
search_bill_button.click()

# accept cookies
cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")
cookies.click()

# get all elements from the dropdown menus AND select by visible text
# select = Select(driver.find_elements(By.NAME, "szlaszolgnev"))
select_text = driver.find_elements(By.NAME, "szlaszolgnev")
dropdown_options_list = select_text[0].text.split('\n')

for choice_name in dropdown_options_list:
    select_option = driver.find_element(By.LINK_TEXT, j)
    print(select_option.text)

# DEF for the funcition
def fast_multiselect(driver, element_id, labels):
    select = Select(driver.find_element_by_id(element_id))
    for label in labels:
        select.select_by_visible_text(label)


# select_option = driver.find_element(By.LINK_TEXT, dropdown_options_list[1])
select_option = driver.find_element(By.PARTIAL_LINK_TEXT, dropdown_options_list[1])
print(select_option.text)

# select.select_by_visible_text('Banana')


# """         ERROR:
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"partial link text","selector":" BKM NONPROFIT Zrt.
# DFaktorház Zrt.
# Díjbeszedő Zrt.
# FCSM Zrt.
# FV Zrt.
# Társ.díj felosz
# """

# driver.close()