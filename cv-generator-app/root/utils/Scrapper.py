from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scrapper:

    useragents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
        "Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
        "Safari/537.36",
    ]

    # Dictionnaires key: Jobboards, value: list des divs
    div_name = {
        "fr.indeed.com": ["jobsearch-JobComponent"],
        "www.monster.fr": ["header-style__JobViewHeaderJobName-sc-c5940466-9",
                           "skill-list-clamped-styles__SkillsContainerInner-sc-5a5d6754-0",
                           "description-styles__DescriptionContainerInner-sc-78eb761c-2"],
        "www.welcometothejungle.com": ["sc-fulCBj", "bRdkhd"],
    }

    @staticmethod
    def get_jobs_infos(url):
        """
        Get descriptions of an offer
        :param url: url of the offer
        :return: array of offer's infos
        """
        infos = []
        i = 0

        # Selenium config
        options = Options()
        options.add_argument("--window-position=-10000,-10000")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        for name in Scrapper.div_name[url.split("/")[2]]:
            # Change user agent to avoid detection
            driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": Scrapper.useragents[i % 2]})
            infos.append(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, name))).text)
            i += 1

        driver.close()
        return infos


    @staticmethod
    def get_list_jobs(url):
        test = '//div[@id="jobsearch-JapanPage"]/div/div[5]/div/div/div[5]/div'

        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        jobs = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, test)))
        jobs_list = jobs.find_elements(By.TAG_NAME, "tbody")
        tmp = []
        for job in jobs_list:
            infos = job.text.split("\n")

            tmp.append({'poste': infos[0], 'entreprise': infos[1], 'lien': job.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")})

        driver.close()
        return tmp
