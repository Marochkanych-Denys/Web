from django.contrib import admin
from .models import Prediction,cards,User

admin.site.register(cards)
admin.site.register(Prediction)
admin.site.register(User)
