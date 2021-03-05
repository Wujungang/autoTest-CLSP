# -*- coding: utf-8 -*-
"""
@Time    : 2021/2/26 16:59
@Author  : wujungang
@File    : test_ModuleManager.py
@Function: 运营中心-Module管理
"""
import os
import time
import uuid
from selenium.webdriver import ActionChains
from selenium import webdriver
import allure
from lxml import etree


@allure.feature('运营中心-APP业务管理-模块登记')
class TestModuleManager:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)

    def screenshot(self):
        address = os.getcwd() + "\\" + "images\\" + str(uuid.uuid1()).replace("-", "") + ".png"
        self.driver.save_screenshot(address)
        file = self.readfile(address)
        return file

    def readfile(self, filename):
        """
        读取文件
        :param filename:
        :return:
        """
        with open(filename, mode="rb") as f:
            file = f.read()
            return file

    def teardown(self):
        address = os.getcwd() + "\\" + "images\\" + str(uuid.uuid1()).replace("-", "") + ".png"
        with allure.step("用例结果截图"):
            # allure.attach(self.driver.save_screenshot(address), "结果页面", allure.attachment_type.PNG)
            allure.attach(self.screenshot(), "结果页面", allure.attachment_type.PNG)
        # self.driver.quit()


    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('测试模块登记-数据全部输入的情况')
    def test_1486(self):
        """
        Module登记-正确输入各个输入项
        :return:
        """
        self.driver.get('http://222.29.77.148:8205/pages/login.html')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/input[1]').send_keys('administrator')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/input[2]').send_keys('letmein')
        action = ActionChains(self.driver)
        action.click_and_hold(self.driver.find_element_by_xpath('//*[@id="mpanel1"]/div/div/div/i')).perform()
        action.move_by_offset(273, 0).perform()
        action.release().perform()
        #点击登录
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/button').click()
        time.sleep(3)
        #点击app业务管理
        self.driver.find_element_by_xpath('//*[@id="seconde-header-nav"]/li[2]').click()
        #点击module管理
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul[2]/ul/li[1]/a/span[1]').click()
        #点击module登记 //*[@id="sidebar"]/ul[2]/ul/li[1]/a/span[1]
        self.driver.find_element_by_xpath('//*[@id="67e84f93-e164-4670-99b7-e6aa29713642"]/a').click()
        #切换到frame
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="content-main"]/iframe[2]'))
        # allure.attach(self.driver.save_screenshot(os.getcwd() + "\\" + "images\\" + str(uuid.uuid1()).replace("-", "") + ".png"), "报错页面", allure.attachment_type.PNG)
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('appman')
        #退出iframe
        self.driver.switch_to.default_content()
        print("ok---200")

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Module发布管理-使用Module名称查询')
    def test_1487(self):
        """
        Module发布管理-使用Module名称查询
        :return:
        """
        # self.driver.get('http://222.29.77.148:8205/pages/login.html')
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/input[1]').send_keys('administrator')
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/input[2]').send_keys('letmein')
        # action = ActionChains(self.driver)
        # action.click_and_hold(self.driver.find_element_by_xpath('//*[@id="mpanel1"]/div/div/div/i')).perform()
        # action.move_by_offset(273, 0).perform()
        # action.release().perform()
        # 点击登录
        # self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/button').click()
        # 点击app业务管理
        self.driver.find_element_by_xpath('//*[@id="seconde-header-nav"]/li[2]').click()
        # 点击module管理
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul[2]/ul/li[2]/a/span[1]').click()
        # 点击module登记 //*[@id="sidebar"]/ul[2]/ul/li[1]/a/span[1]
        self.driver.find_element_by_xpath('//*[@id="43fe6e42-e66f-4c17-9791-fa52e65fafac"]/a').click()
        # allure.attach(self.driver.save_screenshot(os.getcwd() + "\\" + "images\\" + str(uuid.uuid1()).replace("-", "") + ".png"), "报错页面", allure.attachment_type.PNG)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="content-main"]/iframe[2]'))
        self.driver.find_element_by_xpath('//*[@id="app_name"]').send_keys('证书管理')
        #点击查询
        self.driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/div[2]/button[2]').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[5]/div/div/div/div/div/table/tbody/tr/td[1]/a').click()
        time.sleep(3)
        # str = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[5]/div/div/div/div/div/table/tbody/tr/td[1]/a').text
        # tree = etree.HTML(self.driver.page_source)
        # str = tree.xpath('//*[@id="root"]/div/div/div[5]/div/div/div/div/div/table/tbody/tr/td[1]/a')[1].text
        # print(str)
        # 退出iframe
        self.driver.switch_to.default_content()


        # assert str == "证书管理"
