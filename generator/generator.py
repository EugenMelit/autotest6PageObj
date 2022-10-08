import random

from data.data import Person
from faker import Faker
faker_ru = Faker('ru_Ru')
Faker.seed()


def generator_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name= faker_ru.first_name(),
        last_name= faker_ru.last_name(),
        department=faker_ru.job(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
    )

def generator_file():
    path = rf'C:\Users\TSS\Desktop\autotest6PageObj\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path