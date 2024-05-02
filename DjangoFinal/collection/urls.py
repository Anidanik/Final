from django.urls import path
from .views import CollectionApiView

urlpatterns = [
    path('', CollectionApiView.as_view(), name='collection'),
]