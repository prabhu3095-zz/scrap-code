'''
    author : Prabhu Dayal Sahoo
    College : National Institute of Technology Karnataka
    Project Name : SCRAP CODE
    Project Idea : Scraps and stores the best solution code for a given problem code from codechef.com
'''



from optparse import OptionParser
import json
import re
import os,errno
import shutil
from datetime import datetime, timedelta
import time
import urllib
import bs4
import requests
import operator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

base_url = 'http://codechef.com/problems/'

def best_sol():

    problem_name = raw_input('Enter the problem code from www.codechef.com: ')
    
    driver = webdriver.Firefox()
    driver.get(base_url+problem_name)
    print 'Opening Codechef.com...'

    open_submission = driver.find_element_by_xpath("//button[@class='toogle-button fa fa-plus-square-o']")
    open_submission.click()
    
    response = driver.page_source
    soup = bs4.BeautifulSoup(response, 'html.parser')
    
    link = soup.select('div.table-questions a[href^=/viewsolution]')[0]['href']
    sol = str(link)
    
    url = 'https://www.codechef.com' + sol
    driver.get(url)
    print 'Opening %s...' % url
    
    response1 = driver.page_source
    soup1 = bs4.BeautifulSoup(response1, 'html.parser')
    

    f = open('code_%s.txt' % problem_name, 'w')

    print 'Downloading the code...'

    for row in soup1.find_all('ol'):
        for x in row.find_all('li'):
            print >>f, x.text.encode('utf-8')
    print 'Code Downloaded Successfully...'

    f.close()
    
best_sol()
