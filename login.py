#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
import time

URL = 'http://www.maiziedu.com'
username = '1626795207@qq.com'
password = 'abc123456'

def login():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(URL)
    time.sleep(10)
    ele_close = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div/div')
    ele_close.click()
    time.sleep(2)
    ele_login = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/a[2]')
    ele_login.click()
    ele_username = browser.find_element_by_id('id_account_l')
    time.sleep(2)
    ele_username.send_keys(username)
    ele_passwd3 = browser.find_element_by_id('id_password_l')
    time.sleep(2)
    ele_passwd3.send_keys(password)
    ele_login2 = browser.find_element_by_id('login_btn')
    ele_login2.click()
    print(browser.current_url)
    time.sleep(10)
    browser.quit()

if __name__ == '__main__':
    login()