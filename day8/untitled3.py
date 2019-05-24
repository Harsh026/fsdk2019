"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
from selenium import webdriver

from time import sleep
link="https://bidplus.gem.gov.in/bidlists"
driver=webdriver.Firefox(executable_path="/root/forsk/day8/selenium/geckodriver-v0.24.0-linux64/geckodriver-v0.24.0-linux32.tar.gz")
driver.get(link)
_table=driver.find_element_by_class_name('tab-content')




for row in _table.find_element_by_class_name('border block'):
    
    
    sleep(2)
    
    get_school_result = driver.find_element_by_class_name("bid")
    get_school_result.click()
   
    
  