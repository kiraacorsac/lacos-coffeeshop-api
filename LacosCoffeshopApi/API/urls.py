from django.db import router
from django.urls import path, include

from rest_framework import routers
from API.views import FoodViewSet,TagViewSet

router = routers.DefaultRouter()
# monsters will be accesible on
router.register('foods', FoodViewSet) 
router.register('tags',TagViewSet) 


urlpatterns = [
    path('', include(router.urls))
]