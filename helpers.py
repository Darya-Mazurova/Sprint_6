from faker import Faker

class Helper:

    @staticmethod
    def generate_email():
        return Faker().email()