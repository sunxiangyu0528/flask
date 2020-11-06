#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Time: 2020/11/5 17:21
@File:  demo.py
@Author:  sunxiangyu
@Contact:  sunxiangyu@cloudwalk.com
@License: Mulan PSL
"""
from selenium import webdriver


from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://seller.onloon.top")

driver.maximize_window()
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/input[1]").send_keys(15039413934)