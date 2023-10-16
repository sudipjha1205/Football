import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from faker import Faker
from AppTwo.models import Topic,WebPage,AccessRecord,User

topics = ['marketplace','news','music','sports']
fakegen = Faker()

def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):

    for entry in range(n):

        topic = add_topic()

        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        webpg = WebPage.objects.get_or_create(topic=topic,name=fake_name,url=fake_url)[0]

        acc_rec = AccessRecord.objects.get_or_create(webpage=webpg,date=fake_date)[0]

def populate_user(n):
    for entry in range(n):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()

        user = User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)

if __name__ == '__main__':
    print("Populating User Table!!")
    populate_user(n=20)
    print("Populatiion Completed")
