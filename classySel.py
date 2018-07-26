import openpyxl

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


class GeneralSearcher:
    def __init__(self):        
        self.link = 'https://www.stlouis-mo.gov/data/address-search/index.cfm'
        self.driver = webdriver.Firefox()
        
    def search(self,address):
        self.address = address        
        self.addy = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/form/p[1]/input")
        self.search_button = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/form/p[4]/input")

        self.addy.send_keys(self.address)
        self.search_button.click()
        return self.driver.page_source

    def go_back_to_search_page(self):
        self.driver.get(self.link)

    def close_searcher(self):
        self.driver.close() 
    


class DeedSearcher:
    def __init__(self):
        self.link = 'https://mo4laredo.fidlar.com/MOStLouisCity/DirectSearch/#/search'
        self.driver = webdriver.Firefox()

    def search(self,housenumber,street,city,zipcode):
        self.housenumber = housenumber
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.addy_field = self.driver.find_element_by_xpath('//*[@id="houseno"]')
        self.street_field = self.driver.find_element_by_xpath('//*[@id="street"]')
        self.city_field = self.driver.find_element_by_xpath('//*[@id="city"]')
        self.zip_field = self.driver.find_element_by_xpath('//*[@id="zipcode"]')
        self.addy_field.send_keys(self.housenumber)
        self.street_field.send_keys(self.street)
        self.city_field.send_keys(self.city)
        self.zip_field.send_keys(self.zipcode)
##        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.searchbutton = self.driver.find_element_by_css_selector('div.input-block-level:nth-child(9) > button:nth-child(1)')
##        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located((By.ID, "overley")))
##        time.sleep(10)
        self.searchbutton.click()
        return self.driver.page_source
    
    def go_back_to_search_page(self):
        self.driver.get(self.link)
        
    def close_searcher(self):
        self.driver.close() 
    
    

   
        
    
