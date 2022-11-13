from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import QuerySet
# from main.models import Basket
from django.db.models import Sum


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        # if not email:
        #     raise ValueError('The given email must be set')
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class BasketManager(models.Manager):

    def invoice(self, user):
        ticket = self.model._meta.get_field(
            'ticket'
        ).related_model._meta.model.objects.filter(
            is_valid=False, user=user
        )
        price_sum = ticket.aggregate(Sum('price'))
        ticket_id = list(ticket.values_list('id', flat=True))
        return price_sum.get('price__sum'), ticket_id
