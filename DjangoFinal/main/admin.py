from django.contrib import admin
from .models import Games, Publisher, Mechanics,SerialNumber


class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_players', 'publisher')
    list_display_links = ('name', 'publisher')
    search_fields = ('name', 'number_of_players')


admin.site.register(Publisher)
admin.site.register(Games, GamesAdmin)
admin.site.register(SerialNumber)
admin.site.register(Mechanics)