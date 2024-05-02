from django.urls import path
from .views import (GamesView,PublisherView, MainView, RandomGameView, GagaView, CrowdView,
                    LavkaView, StilView, HobbyView, NizaView)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('random_game/', RandomGameView.as_view(), name='random_game'),
    path('games/', GamesView.as_view(), name='games'),
    path('publishers/', PublisherView.as_view(), name='publishers'),
    path('publishers/gaga/', GagaView.as_view(), name='gaga'),
    path('publishers/crowd/', CrowdView.as_view(), name='crowd'),
    path('publishers/lavka/', LavkaView.as_view(), name='lavka'),
    path('publishers/stil/', StilView.as_view(), name='stil'),
    path('publishers/hobby/', HobbyView.as_view(), name='hobby'),
    path('publishers/niza/', NizaView.as_view(), name='niza'),
]

urlpatterns = format_suffix_patterns(urlpatterns)