import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("--disable-popup-blocking ")

driver = webdriver.Chrome(options = options)
nd = webdriver.Chrome(options = options)
url = "https://www.accuweather.com/zh/tw/taiwan-weather"
driver.get(url)
time.sleep(1)
for i in driver.find_elements_by_xpath("/html/body/div/div[4]/div[1]/div/div[2]/div/a"):
    msg = ""  
    if i.find_element_by_class_name("text.title.no-wrap").text[2:] in ["市","縣"]:
        area = i.find_element_by_class_name("text.title.no-wrap").text
        whurl = i.get_attribute("href")
        nd.get(whurl)
        nurl = nd.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/a[2]").get_attribute("href")
        nd.get(nurl)
        time.sleep(2)
        msg += area + "\n"
        for k in nd.find_elements_by_xpath("/html/body/div/div[5]/div[1]/div[1]"):
            elnnum = len(nd.find_elements_by_class_name("accordion-item.hourly-card-nfl.hour.non-ad"))
            for s in range(1,elnnum):
                k.find_element_by_id("hourlyCard" + str(s)).click()
                time.sleep(0.2)
            for a , b , c in zip(k.find_elements_by_xpath("//*/div[1]/div/div[1]/h2/span") , k.find_elements_by_class_name("phrase") ,k.find_elements_by_class_name("temp.metric")):
                msg += f"{a.text} : {b.text} {c.text} \n"
        print(msg)