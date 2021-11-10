from django.db import models

class Prediction(models.Model):
	name = models.CharField(max_length = 100)
	detail = models.CharField(max_length = 2000)

	def __str__(self):
		return f'{self.name}\n {self.detail}'

class cards(models.Model):
    number_of_card=models.CharField(max_length = 16)
    date=models.CharField(max_length = 5)
    cvv=models.CharField(max_length = 3)


class User(models.Model):
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    number_of_card = models.CharField(max_length=16)
    date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)



    def __str__(self):
        return f'{self.id}. {self.name}'