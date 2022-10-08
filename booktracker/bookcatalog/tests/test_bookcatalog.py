'''
    Tests for the BookCatalog API
'''

from django.contrib.auth import get_user_model 
from django.urls import reverse 


CREATE_BOOK_URL = reverse("book-create")

def test_homepage_access():
        url = reverse("home")
        assert url == "/"
