from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance


def index(request):
    text_head = 'На нашем сайте Вы можете получить книги в электронном виде'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all()
    num_instances_availabl = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects.all()
    num_authors = Author.objects.count()
    context = { 'text_head': text_head,
                'books': books, 'num_books': num_books,
                'num_instances': num_instances,
                'num_instances_availabl': num_instances_availabl,
                'authors': authors, 'num_authors': num_authors}

    return render(request, 'catalog/index.html', context)
