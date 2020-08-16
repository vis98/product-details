from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re
import json
import os.path


def get_img_url():
    try:
        img_url = driver.find_element_by_id("landingImage").get_attribute("src")
    except:
        img_url = 'Missing'
    finally:
        return img_url

     
def get_title():
    try:
        subject = driver.find_element_by_xpath('.//span[@id="productTitle"]').text
    except:
        subject = 'Missing'
    finally:
        return subject

     
def get_price():
    try:
        price = driver.find_element_by_xpath('.//span[@id="priceblock_ourprice" or @id="priceblock_saleprice" ]').text
    except:
        price = 'Missing'
    finally:
          return price
     


     
def get_review():
    try:
        review = driver.find_element_by_xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span')

    except:
        review = 'Missing'
    finally:
        return review.get_attribute("innerHTML")


def  get_desc():
     desc=""
     try:
          html_list = driver.find_element_by_id("feature-bullets") 
          items = html_list.find_elements_by_tag_name("li")
          for item in items:
               text = item.text
               desc=desc+" "+text
     except:
          desc = 'Missing'
     finally:
          return desc


driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get('https://www.amazon.in')
driver.find_element_by_id('twotabsearchtextbox').send_keys("men sunglasses")
driver.find_element_by_xpath('//input[@type="submit"]').click()
driver.maximize_window()
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
     
     print("last height is {}".format(last_height))
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

                  
     time.sleep(5)

     new_height = driver.execute_script("return document.body.scrollHeight")
                  
     if new_height == last_height:
          break
     last_height = new_height

     products = driver.find_elements_by_xpath('//a[@class="a-link-normal s-no-outline"]')               



p_links = []
c=0
for p in products:
     p_links.append(p.get_attribute('href'))
     c=c+1

for i in p_links:
     print(i)
     
geeky_file = open('geekyfile.txt', 'a') 
pro=[]
i=0
for c in p_links:
     print(i)
     if i==2:
          break
     else:
          i=i+1
          
     p_dict = {}
     driver = webdriver.Chrome(r'D:/chromedriver.exe')
     try:
          driver.get(c)
     except:
          print("error")
            
     driver.execute_script("window.scrollTo(0,1000);")
     time.sleep(3)
     p_dict['prod_link'] = c
     p_dict['desc']=get_desc()
     p_dict['img_url']=get_img_url()
     p_dict['title'] = get_title()
     p_dict['price'] = get_price()        
     p_dict['review'] = get_review()
     pro.append(p_dict)
     driver.close()
     
     
          

print(json.dumps(pro))
     
     
geeky_file.close()
driver.close()


    


