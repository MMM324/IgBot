from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('http://instagram.com/')
browser = webdriver.Firefox(options=options, executable_path=r'C:\Users\diego\OneDrive\Escritorio\IGBot\geckodriver.exe')

#/