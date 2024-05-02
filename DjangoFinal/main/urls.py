from django.urls import path
from .views import (GamesView,MechanicsApiViewSet,PublisherApiViewSet,
                    PublisherView,MainView, RandomGameView, GagaView, CrowdView,
                    LavkaView,StilView,HobbyView,NizaView)
from rest_framework.urlpatterns import format_suffix_patterns

mechanics_list = MechanicsApiViewSet.as_view({'get':'list'})
mechanics_detail = MechanicsApiViewSet.as_view({'get':'retrieve'})
publisher_list = PublisherApiViewSet.as_view({'get':'list','post':'create'})
publisher_detail = PublisherApiViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})

urlpatterns = [
    path('',MainView.as_view(), name='main'),
    path('random_game/', RandomGameView.as_view(), name='random_game'),
    path('games/',GamesView.as_view(), name='games'),
    path('publishers/',PublisherView.as_view(), name='publishers'),
    path('publishers/gaga/',GagaView.as_view(), name='gaga'),
    path('publishers/crowd/',CrowdView.as_view(), name='crowd'),
    path('publishers/lavka/',LavkaView.as_view(), name='lavka'),
    path('publishers/stil/',StilView.as_view(), name='stil'),
    path('publishers/hobby/',HobbyView.as_view(), name='hobby'),
    path('publishers/niza/',NizaView.as_view(), name='niza'),
    path('mechanicsadm/', mechanics_list, name='mechanic_list'),
    path('publishersadm/<int:pk>', publisher_detail, name='publisher_detail'),
    path('publishersadm/', publisher_list, name='publisher_list'),
    path('mechanicsadm/<int:pk>', mechanics_detail, name='mechanics_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)