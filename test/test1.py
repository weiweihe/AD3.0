#coding=UTF-8
'''
Created on 2016年8月24日

@author: heweiwei
'''

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'BX903JLNLN'
desired_caps['appPackage'] = 'net.easyconn.carman'
desired_caps['appActivity'] =  '.MainActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)

driver.find_element_by_id("net.easyconn.carman:id/iv_music_play_pause").click()


