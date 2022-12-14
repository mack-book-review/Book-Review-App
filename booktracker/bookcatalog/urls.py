from django.urls import path,include
from django.contrib.auth.decorators import login_required
from . import views

from django.contrib.auth.models import User 
from rest_framework import routers, serializers, viewsets 
from .models import Book,BookReview

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','is_staff']
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book 
        fields = ['title','author','synopsis']

class BookReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookReview 
        fields = ["user","book","title","stars","text","date_created"]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookReviewViewSet(viewsets.ModelViewSet):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'bookreviews',BookReviewViewSet)
router.register(r'books',BookViewSet)

urlpatterns = [
    path("",views.home,name="home"),
    path("api/",include(router.urls)),
    path("api-auth/",include("rest_framework.urls")),
    path("search_results/",views.search,name="search"),
    path("login/",views.login,name="login-user"),
    path("register",views.register,name="register-user"),
    path("logout/",views.logout,name="logout-user"),
    path('books',views.BookList.as_view(),name='books'),
    path('books/<int:pk>',views.BookDetail.as_view(),name="book-detail"),
    path('books/create',views.BookCreate.as_view(),name="book-create"),
    path('books/update/<int:pk>',views.BookUpdate.as_view(),name="book-update"),
    path('books/delete/<int:pk>',views.BookDelete.as_view(),name="book-delete"),
    path('add_book/',views.add_book,name="add-book"),
    path('reviews/create/<int:book_id>',views.BookReviewCreate.as_view(),name="review-create")
]
