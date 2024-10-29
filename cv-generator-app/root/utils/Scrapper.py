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

    xpath_dict = {
        "indeed": {
            "poste": ['jobsearch-JobComponent'],
            "liste": ['//div[@id="jobsearch-JapanPage"]/div/div[5]/div/div/div[5]/div'],
        },
        "monster": {
            "poste": ["header-style__JobViewHeaderJobName-sc-c5940466-9",
                               "skill-list-clamped-styles__SkillsContainerInner-sc-5a5d6754-0",
                               "description-styles__DescriptionContainerInner-sc-78eb761c-2"],
            "liste": ["//nav/section/div[2]/div"],
        },
        "welcometothejungle": {
            "poste": ["sc-fulCBj", "bRdkhd"],
            "liste": [],
        }
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
        website = url.split("/")[2].split(".")[1]

        # Selenium config
        options = Options()
        options.add_argument("--window-position=-10000,-10000")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        for name in Scrapper.xpath_dict[website]['poste']:
            # Change user agent to avoid detection
            driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": Scrapper.useragents[i % 2]})
            infos.append(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, name))).text)
            i += 1

        driver.close()
        return infos

    @staticmethod
    def get_list_jobs(jobboard, job, location):
        """
        Get list of jobs
        :param jobboard:
        :param job:
        :param location:
        :return: list of jobs
        """

        base_urls = {
            "indeed": f"https://fr.indeed.com/jobs?q={job}&l={location}",
            "monster": f"https://www.monster.fr/emploi/recherche?q={job}&where={location}&page=1",
        }

        options = Options()
        options.add_argument("--window-position=-10000,-10000")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.get(base_urls[jobboard])

        jobs = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Scrapper.xpath_dict[jobboard]['liste'][0])))

        jobs_list = jobs.find_elements(By.TAG_NAME, "tbody")

        tmp = []
        for job in jobs_list:
            infos = job.text.split("\n")
            tmp.append({'poste': infos[0], 'entreprise': infos[1], 'lien': job.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")})

        driver.close()
        return tmp
