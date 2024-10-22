from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scrapper:

    init = False
    useragents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    ]
    # Dictionnaires key: Jobboards, value: list des divs
    div_name = {
        "fr.indeed.com": ["jobsearch-JobComponent"],
        "www.monster.fr": ["header-style__JobViewHeaderJobName-sc-c5940466-9",
                           "skill-list-clamped-styles__SkillsContainerInner-sc-5a5d6754-0",
                           "description-styles__DescriptionContainerInner-sc-78eb761c-2"],  # Impossible avec Selenium
        #"fr.linkedin.com": ["jobs-search-results__results-list"],
        "www.welcometothejungle.com": ["sc-fulCBj", "bRdkhd"],
    }

    @staticmethod
    def get_jobs_infos(url):

        # Selenium config
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        infos = []

        i = 0  # Nombre de requêtes effectuees
        for name in Scrapper.div_name[url.split("/")[2]]:
            driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": Scrapper.useragents[i % 2]})
            infos.append(WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, name))).text)
            i += 1

        driver.close()
        return infos


