from django.shortcuts import render
from .models import cards,Prediction,User
from django.http import HttpResponseRedirect
from django.urls import reverse
# import json
from django.conf import settings
import redis
import random

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,charset="utf-8",decode_responses=True, db=0)



def begin(request):
	return HttpResponseRedirect(reverse('vanga_app:main'))

def base(request):
	return render(request, 'pages/base.html',{'login': get_User()})
def get_User():
	ID = redis_instance.get('id')
	if ID:
		return User.objects.get(id = int(ID))
	else:
		return False


def prediction(request):
	predict = Prediction.objects.order_by('name')
	rand_predict=random.choice(predict)
	return render(request, 'pages/prediction.html', {'predict': rand_predict, 'login': get_User()})

def no_logg(request):
	return render(request, 'pages/card.html', {'login': get_User()})

def cash(request):
	card0 = cards(
		number_of_card=request.POST['number'],
		date=request.POST['date'],
		cvv=request.POST['cvv'],
	)
	card0.save()
	return prediction(request)

def register(request):
	return render(request, 'pages/registration.html')

def create(request):
	user0 = User(
		name     = request.POST['name'],
		password = request.POST['password'],
		number_of_card = request.POST['number'],
		date = request.POST['date'],
		cvv = request.POST['cvv'],
	)
	card0 = cards(
		number_of_card=request.POST['number'],
		date=request.POST['date'],
		cvv=request.POST['cvv'],
	)

	card0.save()
	user0.save()
	redis_instance.set('id', user0.id)
	return HttpResponseRedirect(reverse('vanga_app:begin'	))

def log_in(request):
	return render(request, 'pages/logging.html',{'login': get_User()})

def check(request):
	try:
		user = User.objects.get(name = request.POST['name'])
		if user.password == request.POST['password']:
			redis_instance.set('id', user.id)
			return HttpResponseRedirect(reverse('vanga_app:main'))
		else:
			return HttpResponseRedirect(reverse('vanga_app:log_in'))
	except:
		return HttpResponseRedirect(reverse('vanga_app:log_in'))

def log_out(request):
	redis_instance.delete('id')
	return HttpResponseRedirect(reverse('vanga_app:begin'))
