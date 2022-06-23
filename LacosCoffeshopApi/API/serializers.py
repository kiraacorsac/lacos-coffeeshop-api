from pkgutil import ImpImporter
from rest_framework import serializers
from API.models import Foods, Tags




    # def validate(self, data):

    #     if data['hitpoints'] < 10 :
    #         raise serializers.ValidationError("hitpoints must be at least 10")
    #     return data        

class TagSerializer (serializers.Serializer):
    id = serializers.IntegerField()
    tag = serializers.CharField(max_length=60)
   


    def create(self, validated_data):
        return Tags.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tag = validated_data.get('tag', instance.tag)
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
        # return Foods.objects.create(**validated_data)
        newfood = Foods.objects.create(name = validated_data["name"],
        image = validated_data["image"],
        likes = validated_data["likes"],
        dislikes = validated_data["dislikes"],
        fave = validated_data["fave"],
        date = validated_data["date"])
        tags = TagSerializer(many=True)
        # tag = validated_data["tags"]
        print(validated_data["tags"])
        # validated_data['tags'] = filter(None, validated_data['tags'])
        if tags:
            for k in tags:
                    k_instance = Tags.objects.get(id=k.id)
                    newfood.tags.set(k_instance)
        return newfood

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.dislikes = validated_data.get('dislikes', instance.dislikes)
        instance.fave = validated_data.get('fave', instance.fave)
        instance.date = validated_data.get('date', instance.date)
        instance.tags.set('tags', instance.tags)
        # c = Tags(name=instance.name , image=instance.image , likes=instance.likes , dislikes=instance.dislikes ,fave=instance.fave ,date=instance.date ,food=instance.food)
        instance.save()
        return instance            