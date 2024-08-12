from django.db import router
from django.urls import path, include

from rest_framework import routers
from API.views import FoodViewSet,TagViewSet,UserViewSet

router = routers.DefaultRouter()
# monsters will be accesible on
router.register('foods', FoodViewSet) 
router.register('tags',TagViewSet) 
router.register('users',UserViewSet) 


urlpatterns = [
    path('', include(router.urls))
]