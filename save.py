import pandas as pd
import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moremore.settings')
django.setup()

from datetime import datetime
from mainpage.models import Competition
from scraping_linkcarrer import scraping_linkcarrer
from scraping_thinkgood import scraping_thinkgood
from scraping_wevity import scraping_wevity

def save_data_to_database(platform, title, url, application_start, application_end):
    if platform == 'linkcarrer':
        for t, u, start, end in zip(title, url, application_start, application_end):
            Competition.objects.create(
                platform=platform,
                title=t,
                url=u,
                application_start=datetime.strptime(start, "%y.%m.%d").strftime("%Y-%m-%d") if start.replace('.', '').isdigit() else '-',
                application_end=datetime.strptime(end,"%y.%m.%d").strftime("%Y-%m-%d") if end.replace('.', '').isdigit() else '-'
            )
    elif platform in ['wevity', 'thinkgood']:
        for t, u, start, end in zip(title, url, application_start, application_end):
            Competition.objects.create(
                platform=platform,
                title=t,
                url=u,
                application_start=datetime.strptime(start,'%Y-%m-%d').strftime("%Y-%m-%d") if start.replace('.', '').isdigit() else '-',
                application_end=datetime.strptime(end,'%Y-%m-%d').strftime("%Y-%m-%d") if end.replace('.', '').isdigit() else '-'
            )

def save_data_to_dataframe(platform, title, url, application_start, application_end):
    if platform == 'linkcarrer':
        data = {
            'platform': platform,
            'title': title,
            'url': url,
            'application_start': [datetime.strptime(start, "%y.%m.%d").strftime("%Y-%m-%d") if start.replace('.', '').isdigit() else '-' for start in application_start],
            'application_end': [datetime.strptime(end, "%y.%m.%d").strftime("%Y-%m-%d") if end.replace('.', '').isdigit() else '-' for end in application_end]
        }
    elif platform in ['wevity', 'thinkgood']:
        data = {
            'platform': platform,
            'title': title,
            'url': url,
            'application_start': [datetime.strptime(start, "%Y-%m-%d") if start.replace('-', '').isdigit() else '-' for start in application_start],
            'application_end': [datetime.strptime(end, "%Y-%m-%d") if end.replace('-', '').isdigit() else '-' for end in application_end]
        }
    df = pd.DataFrame(data)
    df.to_csv(f"{platform}.csv", index=False)

def save_csv_to_database(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # 첫 번째 행은 헤더이므로 건너뜁니다.
            for row in reader:
                platform = row[0]
                title = row[1]
                url = row[2]
                application_start = datetime.strptime(row[3], "%Y-%m-%d")
                application_end = datetime.strptime(row[4], "%Y-%m-%d")
                Competition.objects.create(platform=platform, title=title, url=url, application_start=application_start, application_end=application_end)

if __name__ == "__main__":
    title, url, application_start, application_end = scraping_linkcarrer()
    save_data_to_dataframe('linkcarrer', title, url, application_start, application_end)
    save_csv_to_database("linkcarrer.csv")

    title, url, application_start, application_end = scraping_wevity()
    save_data_to_dataframe('wevity', title, url, application_start, application_end)
    save_csv_to_database("wevity.csv")

    title, url, application_start, application_end = scraping_thinkgood()
    save_data_to_dataframe('thinkgood', title, url, application_start, application_end)
    save_csv_to_database("thinkgood.csv")