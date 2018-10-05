from django.urls import path, include

from rest_framework import routers

from .views import AreaViewSet


router = routers.DefaultRouter()
router.register('areas', AreaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
