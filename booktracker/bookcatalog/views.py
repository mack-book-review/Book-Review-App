from curses.ascii import HT
from wsgiref import validate

#User authentication framework imports
from django.contrib.auth import get_user
from django.contrib import auth
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db.models import Q 

#django shortcuts
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

#other imports
from django.views.generic import ListView,DetailView, DeleteView,CreateView,UpdateView
from django.http import HttpResponse,request
from django.urls import reverse

#imports from within project
from .models import Book, BookReview
from .forms import AddBookForm
from functools import reduce

def get_book_Q(term):
    return Q(title__icontains=term) | Q(author__icontains=term) | Q(synopsis__icontains=term)

def search(request):
    if request.method == "POST":
        search_terms = request.POST['search-terms']
        terms = search_terms.split(" ")
        results = []
        for term in terms:
            results += Book.objects.filter(Q(title__icontains=term) | Q(author__icontains=term) | Q(synopsis__icontains=term))
            return render(request,"bookcatalog/search_results.html",{"results":results})
    else:
        return redirect(home)
    
class BookReviewCreate(CreateView):
    model = BookReview
    fields = ['title','stars','text']
    
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(BookReviewCreate, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self,form):
        form.instance.user = self.user
        form.instance.book = get_object_or_404(Book,pk=self.kwargs["book_id"])
        return super(BookReviewCreate,self).form_valid(form)
    
    def get_success_url(self,**kwargs):
        return "/books/" + str(self.kwargs["book_id"])
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs['book_id']
        context['book'] = get_object_or_404(Book,pk=book_id)
        return context
    
class BookCreate(CreateView):
    model = Book 
    fields = ["title","author","synopsis"]
    success_url = "/books"
    
class BookUpdate(UpdateView):
    model = Book 
    fields = ["title","author","synopsis"]
    success_url = "/books"

class BookDelete(DeleteView):
    model = Book
    success_url = "/books"
    
class BookList(ListView):
    model = Book
    # context_object_name = "books"
    
class BookDetail(DetailView):
    model = Book
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.bookreview_set.all()
        return context  
      
def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            m_title = form.cleaned_data["title"]
            m_author = form.cleaned_data["author"]
            m_synopsis = form.cleaned_data["synopsis"]
            new_book = Book(title=m_title,author=m_author,synopsis=m_synopsis)
            new_book.save()
            return redirect(reverse('books'))
        else:
            messages.info("Error: Book didn't save")
            return redirect(add_book)
    else:
        form = AddBookForm()
        return render(request,"bookcatalog/add_book.html",{"form":form})

def home(request):
    current_user = request.user
    if current_user and current_user.is_authenticated:
        reviews = current_user.bookreview_set.all()
        return render(request,"bookcatalog/index.html",{"reviews": reviews})
    else:
        return redirect(login)
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            m_username = form.cleaned_data.get('username')
            m_password = form.cleaned_data.get('password')
  
            user = auth.authenticate(username=m_username,password=m_password)

            if user is not None:
                auth.login(request,user)
            messages.info(request,"Unable to login {} {}".format(m_username,m_password))
            return redirect(home)
        else:
            messages.info(request,"Unable to login")
            return render(request,"bookcatalog/index.html",{"form":form})
    else:
        form = AuthenticationForm()
        return render(request,"bookcatalog/index.html",{"form":form})


def logout(request):
    auth.logout(request)
    for message in messages.get_messages(request):
        pass
    return redirect(login) 

def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
        
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Email is already taken")
                    return redirect(register)
                else:
                    new_user = User.objects.create_user(username=username,password=password)
                    auth.login(request,new_user)
                    return redirect(home)
            else:
                messages.info(request,'Both passwords are not matching')
                return redirect(register)
        else:
            form = UserCreationForm(request.POST)
            messages.info(request,"Invalid entry")
            return render(request,'bookcatalog/registration.html',{"form":form})
    else:
        form = UserCreationForm()
        return render(request,'bookcatalog/registration.html',{"form":form})
