from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def scraping_linkcarrer():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page_number = 1
    title, url, application_start, application_end = [], [], [], []
    while page_number:
        driver.implicitly_wait(10)
        driver.get(f"https://linkareer.com/list/contest?page={page_number}")

        try:
            driver.find_element(By.CLASS_NAME, "search-result")
            print(f"모든 페이지 스크래핑 완료")
            break
        except NoSuchElementException:
            print(f"{page_number} 페이지 스크래핑 시작")

        titles = driver.find_elements(By.CLASS_NAME, "activity-title")
        urls = driver.find_elements(By.CLASS_NAME, "image-link")
        tmp_urls = []

        for t in titles:
            title.append(t.text)
        for u in urls:
            href = u.get_attribute("href")
            url.append(href)
            tmp_urls.append(href)

        for u in tmp_urls:
            driver.get(u)
            driver.implicitly_wait(10)
            date = driver.find_elements(By.TAG_NAME, "h3")
            if date[3].text != "-":
                application_start.append(date[3].text.split(' ')[0])
                application_end.append(date[3].text.split(' ')[2])
            else:
                application_start.append(None)
                application_end(None)
        
        print(f"{page_number} 페이지 스크래핑 완료")
        page_number += 1

    driver.quit()

    return title, url, application_start, application_end