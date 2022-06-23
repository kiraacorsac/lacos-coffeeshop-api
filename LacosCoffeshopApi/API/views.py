from rest_framework import viewsets, mixins
from API.serializers import FoodSerializer
from API.serializers import TagSerializer
from API.models import Foods, Tags 



class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Foods.objects.all()   

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tags.objects.all()       