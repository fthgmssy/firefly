from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path='/Users/fatihgumussoy/PycharmProjects/firefly/executablebrowser/chromedriver') #geckodriver firefox için ve path kullanıcı için değiştirilebilir.
print("Chrome Browser Invoked")
driver.get("http://hepsiburada.com")
driver.maximize_window()        #browser'ı maximize eder
print(driver.current_url)     #hepsiburada url'ini konsol'a basar.

driver.implicitly_wait(100)

#Giriş yap aşaması

driver.find_element_by_xpath("//*[@id='myAccount']").click()
driver.find_element_by_xpath("//*[@id='login']").click()
driver.find_element_by_id("email").send_keys("denemetest123@hotmail.com")
driver.find_element_by_id("password").send_keys("deneme12345")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/section[1]/div/div[3]/form/div[4]/button").click()

print("Giriş başarıyla yapılmıştır.")

#Ürün araması ve filtreler
driver.find_element_by_xpath("//*[@id='productSearch']").click()
driver.find_element_by_xpath("//*[@id='productSearch']").send_keys("bluetooth kulaklık")
driver.find_element_by_id("buttonProductSearch").click()
driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/div/div/div/div[1]/section/div/div/div/ol/li[2]/ol/li[8]/label").click()
driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/div/div/div/div[1]/section/div/div/div/ol/li[4]/ol/li[4]/label").click()
driver.find_element_by_xpath("/html/body/div[3]/main/div[2]/div/div/div/div/div[1]/section/div/div/div/ol/li[9]/ol/li[1]/label").click()


driver.find_element_by_xpath("//span[.='JBL Free Kablosuz Kulakiçi Kulaklık - Siyah']").click() #Text'e tıklanır.

print("Ürün sepete başarıyla eklenmiştir.")
#ürün detayı-yorumlar ve faydalı kısmı
driver.find_element_by_id("productReviewsTab").click()
driver.find_element_by_xpath("/html/body/div[4]/main/div[3]/section[3]/div/div/div[2]/div/div[2]/div[1]/ul/li[1]/div[6]/p[2]/a[1]").click()


print("Kod başarılı şekilde çalışmıştır.")
#çıkış için
driver.quit()
