from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time  # to add a delay
import numpy as np
import pandas as pd
from datetime import datetime


class ScrapeData:
    __web_url = str
    __item = []
    __names = []
    __ratings = []
    __reviews = []
    __posted_dates = []

    def __init__(self, url):
        self.__web_url = url
        self.__browsewebpage()

        self.__getreviewdata()
        data = self.__preparedataframe()
        self.savetocsv(data)

    def __browsewebpage(self):
        # -- Setting up the webdriver to browse the URL -- #
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--lang=en')

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        driver.get(self.__web_url)

        # clicking the sort button to select the options (to select the newest reviews)
        wait = WebDriverWait(driver, 10)
        sort_bt = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-value=\'Sort\']')))

        sort_bt.click()
        time.sleep(5)

        # clicking the newest value from the dropdown
        wait = WebDriverWait(driver, 10)
        newest_bt = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class=\'fxNQSd\'][2]')))

        newest_bt.click()
        time.sleep(5)

        waiting_time = 5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        number = 0

        while True:
            number = number + 1

            # Scroll down to bottom

            ele = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
            driver.execute_script('arguments[0].scrollBy(0, 5000);', ele)

            # Wait to load page

            time.sleep(waiting_time)

            # Calculate new scroll height and compare with last scroll height
            print(f'last height: {last_height}')

            ele = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

            new_height = driver.execute_script("return arguments[0].scrollHeight", ele)

            print(f'new height: {new_height}')

            if number == 5:
                break

            if new_height == last_height:
                break

            print('cont')
            last_height = new_height

        self.__item = driver.find_elements(By.XPATH,
                                           '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]')

        time.sleep(3)
        return self.__item

    def __getreviewdata(self):
        for i in self.__item:

            button = i.find_elements(By.TAG_NAME, 'button')
            for m in button:
                if m.text == "More":
                    m.click()
            time.sleep(5)

            name = i.find_elements(By.CLASS_NAME, "d4r55")
            stars = i.find_elements(By.CLASS_NAME, "kvMYJc")
            review = i.find_elements(By.CLASS_NAME, "wiI7pd")
            duration = i.find_elements(By.CLASS_NAME, "rsqaWe")

            for j, k, l, p in zip(name, stars, review, duration):
                self.__names.append(j.text)
                self.__ratings.append(k.get_attribute("aria-label"))
                self.__reviews.append(l.text)
                self.__posted_dates.append(p.text)
        return self.__names, self.__ratings, self.__reviews, self.__posted_dates

    def __preparedataframe(self):
        df = pd.DataFrame(
            {'name': self.__names,
             'rating': self.__ratings,
             'text': self.__reviews,
             'duration': self.__posted_dates})

        # removing empty values from the dataframe
        df = df.replace('', np.nan)
        df = df.dropna()
        return df

    def savetocsv(self, dataframe):
        date_time = datetime.now()
        dataframe.to_csv('./data/scrapped.csv', index=False)

