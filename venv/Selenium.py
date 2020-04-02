import time
from selenium.webdriver import Chrome

chromeDrive = 'C:\\temp\\chromedriver.exe'

driver = Chrome(chromeDrive)

driver.get('https://login.11st.co.kr/auth/front/login.tmall')

time.sleep(3)

input_login = driver.find_element_by_id("loginName")
input_login.send_keys("qhrua5514")


input_pw =  driver.find_element_by_id("passWord")
input_pw.send_keys("bogyeum25")

btn=driver.find_element_by_class_name("btn_Atype")

time.sleep(3)



btn.click()

time.sleep(3)
