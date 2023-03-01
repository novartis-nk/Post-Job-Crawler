from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options



def get_cards(urls):
  data = []
  options = Options()
  options.headless = True
  browser = webdriver.Firefox(options=options)
  # for e estekhdam
  if urls[0] != 'none':
    # we use webdriver to get site with dynamic component and design
    url = urls[0]
    browser.get(url)
    #print ("Got the url!")
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    jobs = soup.find_all('li',class_="css-0", limit=10 )
    
    


    # looping through all the cards  
    for job in jobs :
      # get the title, link, icon, desc  
      loc = job.find("span", attrs={"data-testid":"searchSerpJobLocation"}).contents[0]
      company  = job.find("span", attrs={"data-testid":"companyName"}).contents[0]
      title = job.find('a', class_= "chakra-button" ).text
      #print(f'this is the title : {title}')
      link  = job.find('a', class_= "chakra-button" )['href']
      #print(f'this is the link : {link}')
      if job.find("p", attrs={"data-testid":"searchSerpJobDateStamp"}):
        date  = job.find("p", attrs={"data-testid":"searchSerpJobDateStamp"}).contents[0]
        #print(f"this is the date : {date}")
      else : date = ""
        
      data.append(dict(
      company = company,
      title = title,
      link = f'https://www.simplyhired.com{link}',
      date = date,
      site = 'simplyhired',
      loc = loc
      ))
  return data



def tage_name_img(tag):
    return tag.name == 'img' 
