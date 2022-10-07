'''
    Tests for the BookCatalog API
'''

from django.test import TestCase
from django.contrib.auth import get_user_model 
from django.urls import reverse 

from rest_framework.test import APIClient
from rest_framework import status

CREATE_BOOK_URL = reverse("book-create")
CREATE_BOOK_REVIEW = reverse("review-create")


def test_homepage_access(self):
        url = reverse("home")
        assert url == "/"
        
# def create_user(**params):
#     '''Create and return a new user'''
#     return get_user_model().objects.create_user(params)


# class BookCatalogTests(TestCase):
    
#     def setUp(self):
#         self.client = APIClient()
        
#     def test_bookcatalog(self):
#         '''
#             Test
#         '''