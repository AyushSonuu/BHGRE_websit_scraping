import scrapy
from selenium import webdriver
from scrapy_selenium import SeleniumRequest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
class url_extracter_class:
    @classmethod
    def urls_to_send(cls,zip_codes:list):

        url_lst = []
        for zip in zip_codes:
            api_url = f"https://www.bhgre.com/real-estate-agents/{zip}-zip"
            url_lst.append(api_url)

        return url_lst



class AgentDetailsSpider(scrapy.Spider,url_extracter_class):
    name = 'agent_details'
    allowed_domains = ['www.bhgre.com']
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    # start_urls = ['http://www.bhgre.com/']

    def start_requests(self):
        zip_codes = ["92612","11797","07054","90802","23146"]
        # url_lst = url_extracter_class.urls_to_send(zip_codes)
        for zip in zip_codes:
            api_url = f"https://www.bhgre.com/real-estate-agents/{zip}-zip"
            yield scrapy.Request(url = api_url,callback=self.parse,
                                    headers={
                                    'User-Agent': self.user_agent
                                            })

    def parse(self, response):
        # driver = response.request.meta['driver']
        # rsp = Selector(text = str(driver.page_source))
        agent_relative_url_lst = response.xpath("//a[@class='agent-link']/@href").getall()
        # agent_relative_url_lst_50 = agent_relative_url_lst[:5]
        
        i = 0
        for agents_url in agent_relative_url_lst[:51]:
            i = i + 1
            
            agent_absolute_url = f"https://www.bhgre.com{agents_url}"
            # agent_url_lst.append(agent_absolute_url)
            yield scrapy.Request(url = agent_absolute_url,callback=self.agents,
                                    headers={
                                    'User-Agent': self.user_agent
                                            },meta={"Agent url":agent_absolute_url})

            
        
        

    def agents(self,response):
        # driver = response.request.meta['driver']
        body = response.text
        info_dict_str = response.text.split("'application/ld+json'>")[1].strip().replace("\n"," ").split("</script>")[0]
        info_dict = json.loads(info_dict_str)
        adress_dic = info_dict.get("about").get("affiliation").get("address") 
        adress = adress_dic.get("streetAddress")+", "+\
                 adress_dic.get("addressLocality")+", "+\
                 adress_dic.get("addressRegion")+" "+adress_dic.get("postalCode")
        office_name = info_dict.get("about").get("affiliation").get("name")

        
        
        rol_lic = response.xpath("//span[@class='font-11 font-subtler font-fff']/text()").getall()
        role = ""
        lic = ""
        # role_lst=[]
        for i,ro in enumerate(rol_lic):
            r = ro.strip()
            r =   "".join(r.split())
            if r.isalpha():
                role = role +" "+ rol_lic[i] 
            elif "#" in ro:
                lic = lic + ro
        lang = response.xpath("//h2[contains(text(),'Speak')]/parent::node()/ul/li/text()").getall()
        loc_lst = response.xpath("//div[@id='jsAreasServed']/div/ul/li/a/text()").getall()
        yield{
            "Agent url":response.meta.get("Agent url"),
            "Name": info_dict.get("name"),
            "Profile Pic": info_dict.get("thumbnailUrl"),
            "Role" : role,
            "Lic" : lic,
            "Address" : adress,
            "Office Name ": office_name,
            "Zip" : adress_dic.get("postalCode"),
            "Mobile":response.xpath("//*[@id='agent-cover']/div/div/div[2]/div[2]/div[1]/div[2]/a/text()").get(),
            "office" : info_dict.get("about").get("affiliation").get("telephone"),
            "Languages ":" ".join(lang),
            "Locations": ", ".join(loc_lst),
            "Linkedin" : response.xpath("//i[@class ='f-icon f-icon-linkedin-cta f-icon-stack-1x']/parent::node()/parent::node()/@href").get(),
            "Facebook" : response.xpath("//i[@class ='f-icon f-icon-facebook-cta f-icon-stack-1x']/parent::node()/parent::node()/@href").get(),
            "Twitter" : response.xpath("//i[@class ='f-icon f-icon-twitter-cta f-icon-stack-1x']/parent::node()/parent::node()/@href").get(),
            "Instagram" : response.xpath("//i[@class ='f-icon f-icon-instagram-cta f-icon-stack-1x']/parent::node()/parent::node()/@href").get(),
            "Yelp" : response.xpath("//i[@class ='f-icon f-icon-yelp-cta f-icon-stack-1x']/parent::node()/parent::node()/@href").get(),
            
            "Pinterest" :response.xpath("//i[@class ='f-icon f-icon-pinterest-cta f-icon-stack-1x']/parent::node()/parent::node()/@href").get(),

        }