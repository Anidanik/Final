import django.contrib.auth
from .serializers import GameInCollectionSerializer
from .models import GameInCollection, CollectionUser
from main.models import Games
from rest_framework.views import APIView
from rest_framework.response import Response


class CollectionApiView(APIView):

    def get(self,request):
        queryset = GameInCollection.objects.filter(collection__user=request.user).select_related('game','collection')
        serializer = GameInCollectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        id = request.data['id']
        collection, created = CollectionUser.objects.update_or_create(user=request.user)
        game = Games.objects.get(id=id)
        game_in_collection, created = GameInCollection.objects.get_or_create(collection=collection, game=game)
        game_in_collection.save()
        games_in_collection = GameInCollection.objects.filter(collection=collection).select_related('game','collection')
        serializer = GameInCollectionSerializer(games_in_collection, many=True)
        return Response(serializer.data, status=201)

    def delete(self,request):
        id = request.data['id']
        collection = request.user.collection
        game = Games.objects.get(id=id).select_related('game','collection')
        game_in_collection = GameInCollection.objects.get(collection=collection, game=game).select_related('game','collection')
        game_in_collection.delete()
        games_in_collection = GameInCollection.objects.filter(collection=collection).select_related('game','collection')
        serializer = GameInCollectionSerializer(games_in_collection,many=True)
        return Response(serializer.data)