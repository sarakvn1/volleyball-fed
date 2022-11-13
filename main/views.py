from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from main.models import User, Stadium, Team, Ticket, Match, Seat, Basket
from main.payment import payment
from main.serializers import UserSerializer, TeamSerializer, BasketSerializer, StadiumSerializer, MatchSerializer, \
    TicketSerializer, \
    SeatSerializer


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
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        stadiums = Stadium.objects.all()
        serializer = self.serializer_class(stadiums, many=True)
        return Response(serializer.data)


class TicketView(GenericAPIView):
    serializer_class = TicketSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        ticket = Ticket.objects.all()
        serializer = self.serializer_class(ticket, many=True)
        return Response(serializer.data)


class TeamView(GenericAPIView):
    serializer_class = TeamSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        team = Team.objects.all()
        serializer = self.serializer_class(team, many=True)
        return Response(serializer.data)


class MatchView(GenericAPIView):
    serializer_class = MatchSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        match = Match.objects.all()
        serializer = self.serializer_class(match, many=True)
        return Response(serializer.data)


class SeatView(GenericAPIView):
    serializer_class = SeatSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        seat = Seat.objects.all()
        serializer = self.serializer_class(seat, many=True)
        return Response(serializer.data)


class BasketView(GenericAPIView):
    serializer_class = BasketSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        user = request.user.id
        # it will calculate the final amount that user should pay
        # invoice is a method in custom manager
        total_invoice, tickets = Basket.objects.invoice(user=user)
        # this is a function that do the payment and return true or false
        # if everything went well
        # the basket and ticket records will be updated
        payment_result = payment(total_invoice)
        if payment_result is True:
            basket = Basket.objects.filter(ticket_id__in=tickets)
            basket.update(is_paid=True)
            ticket = Ticket.objects.filter(id__in=tickets)
            ticket.update(is_valid=True)
        return Response({"success": True})
