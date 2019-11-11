from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path='/Users/fatihgumussoy/PycharmProjects/firefly/executablebrowser/chromedriver') #chromedriver chrome için ve path kullanıcı için değiştirilebilir.
print("Chrome Browser Invoked")

#Firefox için
# driver = webdriver.Firefox(executable_path='/Users/fatihgumussoy/PycharmProjects/firefly/executablebrowser/geckodriver')
# print("Firefox Browser Invoked")

driver.get("http://hepsiburada.com")
driver.maximize_window()        #browser'ı maximize eder
print(driver.current_url)     #hepsiburada url'ini konsol'a basar.

driver.implicitly_wait(100)

driver.find_element_by_xpath("//*[@id='myAccount']").click()
driver.find_element_by_xpath("//*[@id='login']").click()

driver.find_element_by_id("email").send_keys("denemetest123@hotmail.com")
driver.find_element_by_id("password").send_keys("deneme12345")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/section[1]/div/div[3]/form/div[4]/button").click()

print("Giriş başarıyla yapılmıştır.")

driver.find_element_by_xpath("/html/body/div[3]/main/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div/a/div[4]/button/span/span").click()

print("Ürün başarılı şekilde eklenmiştir.")

driver.find_element_by_id("shoppingCart").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/aside/section/div/div[1]/div[2]/button/span").click()

print("Case 1 başarılı şekilde çalışmıştır.")

driver.close()
driver.quit()