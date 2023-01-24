from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# path = r"C:\Users\Zsolt\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\names.txt"
# chrome_driver = r"C:\Users\Zsolt\Desktop\learningMaterial\Python\Selenium\drivers\chromedriver_win32\chromedriver.exe" # Driver on the Win machine

chrome_driver = r"C:\Drivers\Chrome\chromedriver.exe"   # Driver on the office machine
url_path = r"https://www.dijnet.hu/"
user = "hozsolti"
passwd = "Forzaarsenal96"


# got to the homepage
# service = Service(chrome_driver)
# driver = webdriver.Chrome(service=service)
# driver.get(url_path)
driver = webdriver.Chrome(chrome_driver)
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

# get all elements from the dropdown menus
drop_down_list = driver.find_elements(By.ID, "sopts")
# here I should call the Class, that downloads all the bills
list_element = driver.find_element(By.PARTIAL_LINK_TEXT, str(drop_down_list[1].text))

for i in drop_down_list:
    print(i.text)

def fucker():
    pass

# """         ERROR:
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"partial link text","selector":" BKM NONPROFIT Zrt.
# DFaktorház Zrt.
# Díjbeszedő Zrt.
# FCSM Zrt.
# FV Zrt.
# Társ.díj felosz
# """

# driver.close()