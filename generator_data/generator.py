import random
from data.data_for_info import properties_for_information
from faker import Faker
faker = Faker('en.US')
Faker.seed()


def generator_info():
    yield properties_for_information(
        full_name=faker.first_name() + ' ' + faker.last_name(),# + ' ' + faker.middle_name(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=random.randint(22, 55),
        mobile_number=random.randint(1000000000, 9999999999),
        salary=random.randint(7500, 15000),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )


def generator_subject():
    subject = ['English', 'Math', 'Physics', 'Chemistry', 'Computer Science', 'Economics', 'Arts', 'Social Studies',
               'Arts', 'History', 'Civics', 'Biology', 'Accounting', 'Hindi']
    return subject[random.randint(0, 13)]
