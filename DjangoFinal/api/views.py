from django.shortcuts import render
from .serializers import MechanicsSerializer, PublisherSerializer
from rest_framework import viewsets
from main.models import Mechanics, Publisher
from rest_framework import permissions


class MechanicsApiViewSet(viewsets.ModelViewSet):
    queryset = Mechanics.objects.all()
    serializer_class = MechanicsSerializer
    permission_classes = [permissions.IsAdminUser]


class PublisherApiViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAdminUser]