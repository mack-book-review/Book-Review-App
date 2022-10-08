'''
    Tests for the BookCatalog API
'''
from django.test import TestCase
from django.contrib.auth import get_user_model 
from django.urls import reverse 

from rest_framework.test import APIClient
from rest_framework import status

CREATE_BOOK_URL = reverse("book-create")

def test_homepage_access():
        url = reverse("home")
        assert url == "/"
