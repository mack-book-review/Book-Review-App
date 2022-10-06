from django import forms 



class AddBookForm(forms.Form):
    title = forms.CharField(label="Title",max_length=100)
    author = forms.CharField(label="Authors",max_length=100)
    synopsis = forms.CharField(label="Synopsis",max_length=1000)