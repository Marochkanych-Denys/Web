from django.urls import path
from . import views

app_name = 'vanga_app'
urlpatterns = [
	path('',views.begin, name = 'begin'),

	path('main',views.base, name = 'main'),

	path('prediction',views.prediction, name = 'prediction'),
	path('no_logg',views.no_logg, name = 'no_logg'),
	path('cash',views.cash, name = 'cash'),
	path('register',views.register, name = 'register'),
	path('create',views.create, name = 'create'),
	path('log_in',views.log_in, name = 'log_in'),
	path('check',views.check, name = 'check'),
	path('log_out',views.log_out, name = 'log_out'),
]