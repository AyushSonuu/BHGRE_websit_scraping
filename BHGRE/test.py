from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# options.add_argument("--headless")
# driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
# urls_lst = []
# zip_codes = ["92612","11797","07054","90802","23146"]
# for zip in zip_codes:
#     driver.get("https://www.bhgre.com/real-estate-agents")
#     inp = driver.find_element(By.XPATH,'//*[@id="agentSearch"]')
#     inp.send_keys(zip)
#     inp.send_keys(Keys.ENTER)
#     url = driver.current_url
#     urls_lst.append(url)
# print(urls_lst)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
# driver.get("https://www.bhgre.com/real-estate-agents")
# inp = driver.find_element(By.XPATH,'//*[@id="agentSearch"]')
# inp.send_keys("92612")
# inp.send_keys(Keys.ENTER)
# print(driver.current_url)
# from scrapy_selenium import SeleniumRequest

# i = 0
# k = 2
# for j in range(10):
#     i = i +1
#     k = k + 2
#     print(i,k)

# https://www.bhgre.com/Better-Homes-and-Gardens-Real-Estate-Champions-45791c/Miriam-Rey-5127617a
# https://www.bhgre.com/real-estate-agents/92612-zip

zip_codes = ["92612","11797","07054","90802","23146"]
url_lst = []
for zip in zip_codes:
    api_url = f"https://www.bhgre.com/real-estate-agents/{zip}-zip"
    url_lst.append(api_url)
print(url_lst)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# options.add_argument("--headless")
# driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

