from django.urls import path 
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path("",views.home,name="home"),
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
