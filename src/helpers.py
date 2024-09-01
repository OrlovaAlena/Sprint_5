import random


class GenerateUser:

    @staticmethod
    def generate_email():
        add = random.randint(100, 999)
        domain = random.choice(['@mail.ru', '@gmail.com', '@yandex.ru'])
        email = 'orlovaalena13' + str(add) + domain
        return email

    @staticmethod
    def generate_password():
        add = random.randint(10, 99)
        password = 'pass' + str(add)
        return password
