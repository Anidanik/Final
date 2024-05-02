from django.contrib import admin
from main.models import Games
from .models import GameInCollection, CollectionUser

admin.site.register(CollectionUser)
admin.site.register(GameInCollection)

