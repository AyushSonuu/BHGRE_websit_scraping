# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from scrapy import Selector
# from selenium import webdriver
# # from shutil import which
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# class Urls_extr():
#     @classmethod
#     def main_page_url(cls,zip_codes:list):
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach",True)
#         options.add_argument("--headless")
#         driverr = webdriver.Chrome(options=options,service= Service(ChromeDriverManager().install()))
#         driverr.maximize_window()
#         urls_lst = []
#         for zip in zip_codes:
#             driverr.get("https://www.bhgre.com/real-estate-agents")
#             inp = driverr.find_element(By.XPATH,'//*[@id="agentSearch"]')
#             inp.send_keys(zip)
#             inp.send_keys(Keys.ENTER)
#             url = driverr.current_url
#             urls_lst.append(url)

#         return urls_lst