from rest_framework import serializers
from API.models import Foods, Tags

class TagSerializer (serializers.Serializer):
    # id = serializers.IntegerField()
    tag = serializers.CharField(max_length=60)
   
    def create(self, validated_data):
        return Tags.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tag = validated_data.filter('tag', instance.tag)
        instance.save()
        return instance        

class FoodSerializer (serializers.Serializer):
    name = serializers.CharField(max_length=60)
    image = serializers.CharField()
    likes = serializers.IntegerField()  
    dislikes = serializers.IntegerField()  
    fave= serializers.BooleanField() 
    date = serializers.DateField()
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Tags.objects.all())

    def create(self, validated_data):
        newfood = Foods.objects.create(
            name = validated_data["name"],
            image = validated_data["image"],
            likes = validated_data["likes"],
            dislikes = validated_data["dislikes"],
            fave = validated_data["fave"],
            date = validated_data["date"],
        )
        newfood.tags.set(validated_data["tags"])
        return newfood

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.dislikes = validated_data.get('dislikes', instance.dislikes)
        instance.fave = validated_data.get('fave', instance.fave)
        instance.date = validated_data.get('date', instance.date)
        instance.tags.set(validated_data["tags"])
        instance.save()
        return instance            

    # def delete(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.likes = validated_data.get('likes', instance.likes)
    #     instance.dislikes = validated_data.get('dislikes', instance.dislikes)
    #     instance.fave = validated_data.get('fave', instance.fave)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.tags.set(validated_data["tags"])
    #     instance.delete()
    #     return instance            