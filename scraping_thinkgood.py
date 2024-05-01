from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from save import save_data_to_database

def scraping_thinkgood():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page_number = 1
    title, url, application_start, application_end = [], [], [], []
    while True:
        if page_number == 1:
            driver.implicitly_wait(10)
            driver.get("https://www.thinkcontest.com/thinkgood/user/contest/index.do#PxyyoRLHIcgvNg6HiHNz_uA4QOthhmxuMkOJ-8OGsYHuum-XS7oXTXHj_WQpSdho7EnVynWoiuBwl84H1ChINGL0PwCVS2cspmoqCGi-qpZY6T5M_ZxBwx9fWgmwB-cK")
        titles = driver.find_elements(By.CLASS_NAME, "tit")
        contents = driver.find_elements(By.CLASS_NAME, "contentitem")
        
        print(f"{page_number} 페이지 스크래핑 시작")

        for t in titles:
            if t.tag_name == 'div':
                title.append(t.text)

        for c in contents:
            driver.implicitly_wait(3)
            c.click()
            url.append(driver.current_url)
            driver.back()

        for c in contents:
            date = c.find_elements(By.TAG_NAME, 'td')[4].text
            application_start.append(date.split(' ')[0])
            application_end.append(date.split(' ')[2])

        print(f"{page_number} 페이지 스크래핑 완료")

        try:
            driver.implicitly_wait(3)
            arrow_next_element = driver.find_element(By.CSS_SELECTOR, '#pagination1 > a.next')
            arrow_next_element.click()
        except NoSuchElementException:
            print(f"모든 페이지 스크래핑 완료")
            break
        page_number += 1

    driver.quit()

    return title, url, application_start, application_end


if __name__ == "__main__":
    title, url, application_start, application_end = scraping_thinkgood()
    save_data_to_database('thinkgood', title, url, application_start, application_end)