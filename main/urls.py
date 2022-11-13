
from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]