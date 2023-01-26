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
provider_dropdown_options_list = select_text[0].text.split('\n')

""" INNEN LEHET MAJD HíVNI A CLASS-T """

# //*[contains(@value, "Díjbeszedő Zrt.")]
# for provider in provider_dropdown_options_list:
#     # provider_string = '//*[contains(@value, "{}")]'.format(provider.strip())
#     dropdown_option = driver.find_element(By.XPATH, '//*[contains(@value, "{}")]'.format(provider.strip()))
#     print(dropdown_option.text)


dropdown_option = driver.find_element(By.XPATH, '//*[contains(@value, "{}")]'.format(provider_dropdown_options_list[0]
                                                                                     .strip()))

# keresés gombot megtalálni:
provider_submit_button = driver.find_element(By.ID, "submit")
provider_submit_button.click()

# coutn how many rows are in the reached table
count = driver.find_elements_by_xpath("//table/tbody/tr")
# print(len(count))
lista = range(0, len(count))                                     # ezt lehetne használni a táblázat hosszának megállapításához

# for r_number in lista:
#     """ Evvel végig lehet majd lépegetni az egyes szolgáltatóknál lévő számla sorokon. """
#     id_text = "r_{}".format(r_number)
#     # print(id_text)
#     row = driver.find_element(By.ID, id_text)
#     row.click()
#     break

"""Megkeresem a számla letöltéséhez szükséges linket és átmegyek a letöltő oldalra"""
download_nav_link = driver.find_element(By.XPATH, '//*[contains(@href, "/ekonto/control/szamla_letolt")]')
download_nav_link.click()

""" tényleges számla letöltés """
"""<a href="szamla_pdf?1113233069" class="" target="_self">Számla nyomtatható verziója (PDF) - Hiteles számla</a>"""
download_bill = driver.find_element(By.LINK_TEXT, "Számla nyomtatható verziója (PDF) - Hiteles számla")
download_bill.click()

# driver.close()


