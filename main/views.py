from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from main.models import User
from main.serializers import UserSerializer, StadiumSerializer, MatchSerializer, TicketSerializer, SeatSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class StadiumView(GenericAPIView):
    serializer_class = StadiumSerializer

    def post(self, request):
        return Response("")


class TicketView(GenericAPIView):
    serializer_class = TicketSerializer

    def post(self, request):
        return Response("")


class MatchView(GenericAPIView):
    serializer_class = MatchSerializer

    def post(self, request):
        return Response("")


class SeatView(GenericAPIView):
    serializer_class = SeatSerializer

    def post(self, request):
        return Response("");
