from django.contrib import admin
from .models import Games, Publisher, Mechanics, SerialNumber

admin.site.register(Publisher)
admin.site.register(Games)
admin.site.register(SerialNumber)
admin.site.register(Mechanics)