__author__ = 'JeffChow'

from selenium import webdriver

pathToDriver = "c:\Dev\programs\chrome\chromedriver.exe"
browser = webdriver.Chrome(pathToDriver)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

