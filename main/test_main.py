import json
import time
from types import SimpleNamespace
import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from loguru import logger

from main.models import *


@pytest.mark.django_db
def test_create_stadium_with_force_authentication_should_pass():
    user = baker.make('main.User', id=1, username="lauren")
    client = APIClient()
    data = {
        "name": "string",
        "rows": 10,
        "columns": 10
    }
    client.force_authenticate(user=user)
    response = client.post('/stadium', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_team_with_force_authentication_should_pass():
    user = baker.make('main.User', id=1, username="lauren")
    client = APIClient()
    data = {
        "name": "string",
        "details": {}
    }
    client.force_authenticate(user=user)
    response = client.post('/team', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_match_with_force_authentication_should_pass():
    user = baker.make('main.User', id=1, username="lauren")
    _ = baker.make('main.Team', id=1)
    _ = baker.make('main.Team', id=2)
    client = APIClient()
    data = {
        "name": "string",
        "available_seats": 100,
        "home_team": 1,
        "away_team": 2,
        "stadium": 1
    }
    client.force_authenticate(user=user)
    response = client.post('/match', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_seat_with_force_authentication_should_pass():
    user = baker.make('main.User', id=1, username="lauren")
    _ = baker.make('main.Match', id=1)
    client = APIClient()
    data = {
        "row": 20,
        "column": 10,
        "is_occupied": False,
        "match": 1
    }
    client.force_authenticate(user=user)
    response = client.post('/seat', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_ticket_with_force_authentication_should_pass():
    user = baker.make('main.User', id=1, username="lauren")
    _ = baker.make('main.seat', id=1)
    client = APIClient()
    data = {
        "is_valid": False,
        "price": 100,
        "user": 1,
        "seat": 1
    }
    client.force_authenticate(user=user)
    response = client.post('/ticket', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_ticket_with_force_authentication_should_pass():
    user = baker.make('main.User', id=1, username="lauren")
    _ = baker.make('main.ticket', id=1)
    client = APIClient()
    data = {
        "is_paid": False,
        "user": 1,
        "ticket": 1
    }

    client.force_authenticate(user=user)
    response = client.post('/basket', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200
