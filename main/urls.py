from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import UserViewSet,BasketView, StadiumView, TeamView, TicketView, SeatView, MatchView

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('stadium', StadiumView.as_view()),
    path('team', TeamView.as_view()),
    path('ticket', TicketView.as_view()),
    path('seat', SeatView.as_view()),
    path('match', MatchView.as_view()),
    path('basket',BasketView.as_view()),
]
