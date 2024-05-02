from .models import Games, Publisher, Mechanics , SerialNumber
from rest_framework import serializers


class MechanicsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mechanics = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Mechanics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Mechanics = validated_data.get('mechanics', instance.mechanics)
        instance.save()
        return instance


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    publisher = serializers.CharField(max_length=30)
    count = serializers.IntegerField()

    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.count = validated_data.get('count', instance.count)
        instance.save()
        return instance


class SerialNumberSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=9)

    def create(self, validated_data):
        return SerialNumber.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance
