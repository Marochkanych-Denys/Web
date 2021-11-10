from django.test import TestCase
from .models import Prediction, cards, User



class Test(TestCase):
    def setUp(self) -> None:
        self.User = User


    def test_1(self):
        user = User()
        user.name = 'test'
        user.password = 'qwe123'
        user.number_of_card = '1234567891231234'
        user.date = '02/12'
        user.cvv = '123'
        user.save()

        user_control=User.objects.get(name = 'test' )
        self.assertEqual(user_control.password, user.password)
        self.assertEqual(user_control.number_of_card, user.number_of_card)
        self.assertEqual(user_control.date, user.date)
        self.assertEqual(user_control.cvv, user.cvv)

