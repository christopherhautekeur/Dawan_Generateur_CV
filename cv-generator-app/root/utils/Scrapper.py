from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scrapper:

    chrome_options = Options()

    @staticmethod
    def get_jobs_infos(url):
        driver = webdriver.Chrome(options=Scrapper.chrome_options)
        driver.get(url)
        infos = (WebDriverWait(driver, 3)
                 .until(EC.element_to_be_clickable((By.CLASS_NAME, "jobsearch-JobComponent"))).text)
        driver.close()
        return infos


