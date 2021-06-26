from django.test import TestCase

# Create your tests here.

import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.parametrize('param', [
    'login',
    'register',
    'login',
    'register',
    'patient_reg',
    'doctor_reg',
])
def test_render_views(client, param):
    temp_url = reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200
