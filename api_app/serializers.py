from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=200)
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

