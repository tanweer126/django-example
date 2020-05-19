import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django

django.setup()

from second_app.models import User
from faker import Faker

fakgen = Faker()

def populate(N=6):
    
    for i in range (N):
        fake_name = fakgen.name().split()
        first = fake_name[0]
        last = fake_name[1]
        emaill = fakgen.email()

        users = User.objects.get_or_create(first_name=first, last_name=last, email=emaill)

if __name__ == '__main__':
    print("populaitng scripts")
    populate(5)
    print("population complete")
