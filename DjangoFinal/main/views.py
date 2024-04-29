from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions
from .serializers import MechanicsSerializer, PublisherSerializer
from .models import Games, Publisher, Mechanics
from rest_framework import viewsets


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'main/Main.html'


class RandomGameView(LoginRequiredMixin, TemplateView):
    template_name = 'main/random_game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Games.objects.order_by('?')[:1].select_related('publisher','serial_number')
        return context


class GamesView(LoginRequiredMixin, TemplateView):
    template_name = 'main/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = Games.objects.all().select_related('publisher','serial_number')
        return context


class PublisherView(LoginRequiredMixin, TemplateView):
    template_name = 'main/publishers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.all()
        return context


class CrowdView(PublisherView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.filter(Q(publisher='Crowd games'))
        context['games'] = Games.objects.filter(Q(publisher__publisher='Crowd games'))
        return context


class LavkaView(PublisherView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.filter(Q(publisher='Lavka Games'))
        context['games'] = Games.objects.filter(Q(publisher__publisher='Lavka Games'))
        return context


class StilView(PublisherView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.filter(Q(publisher='Стиль жизни'))
        context['games'] = Games.objects.filter(Q(publisher__publisher='Стиль жизни'))
        return context


class HobbyView(PublisherView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.filter(Q(publisher='Hobby Games'))
        context['games'] = Games.objects.filter(Q(publisher__publisher='Hobby Games'))
        return context


class NizaView(PublisherView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.filter(Q(publisher='Niza Games'))
        context['games'] = Games.objects.filter(Q(publisher__publisher='Niza Games'))
        return context


class GagaView(PublisherView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.filter(Q(publisher='Gaga Games'))
        context['games'] = Games.objects.filter(Q(publisher__publisher='Gaga Games'))
        return context


class MechanicsApiView(viewsets.ModelViewSet):
    queryset = Mechanics.objects.all()
    serializer_class = MechanicsSerializer
    permission_classes =[permissions.IsAdminUser]


class PublisherApiViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes =[permissions.IsAdminUser]
