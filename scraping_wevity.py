from bs4 import BeautifulSoup
import requests
import time

from save import save_data_to_database

def scraping_wevity():
    page_number = 1
    title, url, application_start, application_end = [], [], [], []

    while page_number:
        response = requests.get(f"https://www.wevity.com/?c=find&s=1&mode=ing&gp={page_number}")
        soup = BeautifulSoup(response.text, 'html.parser')
        element_tit = soup.find_all(class_="tit")[1:]

        if len(element_tit) == 0:
            print(f"모든 페이지 스크래핑 완료")
            break
        print(f"{page_number} 페이지 스크래핑 시작")

        for e in element_tit:
            text = ''
            for element in e.find('a').contents:
                if element.name == 'span':
                    continue
                text += str(element).strip()
            title.append(text)
            url.append('https://www.wevity.com/' + (e.find('a').get('href')))

        for u in url:
            time.sleep(0.3)
            response = requests.get(u)
            soup = BeautifulSoup(response.text, 'html.parser')
            element_dday_area = soup.find_all('li', class_="dday-area")
            for e in element_dday_area:
                text = ''
                for element in e.contents:
                    if element.name == 'span':
                        continue
                    text += str(element).strip()
                application_start.append(text.split(' ')[0])
                application_end.append(text.split(' ')[2])

        time.sleep(0.3)
        print(f"{page_number} 페이지 스크래핑 완료")
        page_number += 1

    return title, url, application_start, application_end


if __name__ == "__main__":
    title, url, application_start, application_end = scraping_wevity()
    save_data_to_database('위비티', title, url, application_start, application_end)