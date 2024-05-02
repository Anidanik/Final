from .models import GameInCollection
from rest_framework import serializers


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)


class GameInCollectionSerializer(serializers.Serializer):

    class Meta:
        model = GameInCollection
        fields = ('game')

    def to_representation(self, instance):
        data = GameSerializer(instance.game).data
        return data

