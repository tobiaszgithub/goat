import os
cwd = os.getcwd()
print(cwd)
from selenium import webdriver

browser = webdriver.Chrome(executable_path='../chromedriver.exe')
browser.get('http://localhost:8000')
assert 'Django' in browser.title