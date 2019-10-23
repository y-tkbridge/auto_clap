#!/usr/local/bin/python3
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#システムモジュール
from time import sleep
import datetime, os

def openUnipos(browser: webdriver):

    browser.get('https://unipos.me/login')
    
    # input login id
    login_id_xpath = '//*[@id="content"]/div/div/div[2]/input[1]'
    browser.find_element_by_xpath(login_id_xpath).send_keys(os.getenv('LOGIN_ID'))
 
    #input login password
    login_password_xpath = '//*[@id="content"]/div/div/div[2]/input[2]'
    browser.find_element_by_xpath(login_password_xpath).send_keys(os.getenv('LOGIN_PASSWORD'))

    #click login button
    browser.find_element_by_class_name('login_btn').click()

    #ページの読み込み自家を稼ぐ
    sleep(10)
    #execute clap hand(投稿の上位 n 件に拍手する)
    for clap_count in range(1,2):
        clap_pass_xpath = '//*[@id="content"]/div[7]/div/div/div/div[2]/div[5]/div[{}]/div[1]/div[3]/div[3]/div[2]/a'.format(clap_count)
        browser.find_element_by_xpath(clap_pass_xpath).click()

if __name__ == '__main__':
    try:
        #browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        #browser = webdriver.Chrome()   # 普通のChromeを制御する場合

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # Googleで検索実行
        # execSearch(browser)

        openUnipos(browser)

    finally:
        # 終了
        sleep(5)
        browser.close()
        browser.quit()

