from rest_framework import viewsets, mixins
from API.serializers import FoodSerializer
from API.serializers import TagSerializer, UserSerializer
from API.models import Foods, Tags 
from django.contrib.auth.models import User



class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Foods.objects.all()   

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tags.objects.all()    

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()     