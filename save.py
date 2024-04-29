import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moremore.settings')
django.setup()

from datetime import datetime
from mainpage.models import Competition

def save_data_to_database(platform, title, url, application_start, application_end):
    for t, u, start, end in zip(title, url, application_start, application_end):
        Competition.objects.create(
            platform=platform,
            title=t,
            url=u,
            application_start=datetime.strptime(start, "%y.%m.%d").strftime("%Y-%m-%d"),
            application_end=datetime.strptime(end,"%y.%m.%d").strftime("%Y-%m-%d")
        )