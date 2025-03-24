from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'genre']

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title.strip():
            raise forms.ValidationError("Title cannot be empty.")
        return title

    def clean_author(self):
        author = self.cleaned_data['author']
        if not author.strip():
            raise forms.ValidationError("Author cannot be empty.")
        return author

    def clean_year(self):
        year = self.cleaned_data['year']
        if year <= 0:
            raise forms.ValidationError("Year must be a positive number.")
        return year
