import os
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_django_playground.settings')

import django

django.setup()

from greeting_app.models import Topic, WebPage, AccessRecord

# Fake Population Script
faker_generator = Faker()
topics = ['Afrikaans', 'English', 'Spanish', 'German']


def add_topic():
    topic = Topic.objects.get_or_create(name=random.choice(topics))[0]
    topic.save()
    return topic


def populate(n=5):
    for entry in range(n):
        topic = add_topic()

        fake_url = faker_generator.url()
        fake_date = faker_generator.date()
        fake_name = faker_generator.company()

        web_page = WebPage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]

        access_record = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating Script:')
    populate(20)
    print('Populating complete!')
