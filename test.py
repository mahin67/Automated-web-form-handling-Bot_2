import time
from  django.test import LiveServerTestCase
from  selenium import webdriver
from selenium.webdriver.common.keys import  Keys


class LoadFormtest(LiveServerTestCase):

    def testLoad(self):

        driver= webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')

        time.sleep(444444)

