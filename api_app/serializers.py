from .models import WatchList,StreamPlatform
from rest_framework import serializers

def name_length(value):
    if len(value) < 4:
        raise serializers.ValidationError("name length tooooooo short")
    return value


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"

    def get_len_title(self, data):
        return str(len(data.title))


    # name = serializers.CharField(max_length=64,validators=[name_length])
    # description = serializers.CharField(max_length=200)
    # active = serializers.BooleanField(default=True)
    #
    # # def validate_name(self,value):
    # #     if len(value)<3:
    # #         raise serializers.ValidationError("name length too short")
    # #     return value
    #
    # def validate(self, object):
    #     if object['name'] == object['description']:
    #         raise serializers.ValidationError("name and description should be different")
    #     return object
    #
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    #
