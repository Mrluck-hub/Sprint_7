import random
import string

class PayloadGenerator:
    @staticmethod
    def random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    @classmethod
    def courier_payload(cls):
        return {
            "login": cls.random_string(),
            "password": "password123",
            "firstName": cls.random_string()
        }
    
    ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
        "BLACK"
        ]
    }
