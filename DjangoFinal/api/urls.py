from django.urls import path
from .views import (MechanicsApiViewSet, PublisherApiViewSet)

from rest_framework.urlpatterns import format_suffix_patterns

mechanics_list = MechanicsApiViewSet.as_view({'get': 'list', 'post': 'create'})
mechanics_detail = MechanicsApiViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
publisher_list = PublisherApiViewSet.as_view({'get': 'list', 'post': 'create'})
publisher_detail = PublisherApiViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('mechanics/', mechanics_list, name='mechanic_list'),
    path('publishers/<int:pk>', publisher_detail, name='publisher_detail'),
    path('publishers/', publisher_list, name='publisher_list'),
    path('mechanics/<int:pk>', mechanics_detail, name='mechanics_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)