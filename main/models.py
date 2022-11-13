import json

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

from loguru import logger
from django.db.models.signals import post_delete
from django.dispatch import receiver

from main.managers import UserManager, BasketManager


class BaseModel(models.Model):
    created_time = models.DateTimeField('Created Time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated Time', auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    location = models.JSONField(blank=True, null=True, default=dict)
    USERNAME_FIELD = 'username'

    objects = UserManager()

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.id}-{self.username}"


class Stadium(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    rows = models.PositiveIntegerField(blank=False, null=False, default=1)
    columns = models.PositiveIntegerField(blank=False, null=False, default=10)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Team(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    details = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Match(BaseModel):
    name = models.CharField(max_length=50)
    home_team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE, related_name='away_team')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id}-{self.name}"


class Seat(BaseModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    row = models.PositiveIntegerField(blank=False, null=False, default=1)
    column = models.PositiveIntegerField(blank=False, null=False, default=1)
    is_occupied = models.BooleanField(default=False)


class Ticket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=False)
    price = models.PositiveIntegerField(blank=False, null=False)


class Basket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    objects = BasketManager()
