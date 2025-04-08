from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# View to list all books or filter them by search query
def book_list(request):
    query = request.GET.get('q')  # Get search query from URL parameters
    if query:
        # If query exists, filter books with title containing the query (case-insensitive)
        books = Book.objects.filter(title__icontains=query)
    else:
        # Otherwise, fetch all books
        books = Book.objects.all()
    # Render the list template with the books and query
    return render(request, 'books/book_list.html', {'books': books, 'query': query})

# View to add a new book
def book_create(request):
    # Create form instance using POST data (if available)
    form = BookForm(request.POST or None)
    if form.is_valid():
        # Save the new book to the database if form is valid
        form.save()
        return redirect('book_list')  # Redirect to book list after saving
    # Render the book form template with 'Add' action label
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Add'})

# View to update an existing book
def book_update(request, pk):
    # Get the book object by primary key or return 404 if not found
    book = get_object_or_404(Book, pk=pk)
    # Create form instance with POST data and bind it to the book instance
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        # Save changes to the book if form is valid
        form.save()
        return redirect('book_list')  # Redirect to book list after saving
    # Render the book form template with 'Update' action label
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Update'})

# View to delete an existing book
def book_delete(request, pk):
    # Get the book object by primary key or return 404 if not found
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Delete the book only on POST request (confirmation submitted)
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    # Render a confirmation page before deleting
    return render(request, 'books/book_confirm_delete.html', {'book': book})
