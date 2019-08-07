from django.shortcuts import render,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,
                                 CreateView, 
                                 DeleteView,
                                 DetailView,
                                 UpdateView
                                 )
from .models import Book
from django.db.models import Q

def home(request):
    return render(request,'library/home.html')
    
class BookListView(ListView):
    model = Book
    template_name = 'library/booklist.html'
    context_object_name = 'books'
    ordering = ['-bookname']

    def get(self, request):
        query = request.GET.get('q', None)
        books = Book.objects.all()
        if query is not None:
            books = books.filter(Q(bookname__icontains=query))
        return render(request,'library/booklist.html',books)

class BookDetailView(DetailView):
    model = Book

def booklist(request):
    query = request.GET.get('q', None)
    qs = Book.objects.all()
    if query is not None:
        qs = qs.filter(Q(bookname__icontains=query))
    context = {
        'books': qs
    }

    return render(request,'library/booklist.html',context)

class AddBookCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Book
    fields = ['booktype','bookname','location','authorname','publisher','year_publish', 'tags','bookstatus']

    def form_valid(self, form):
        # from.instance.authorname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request,f'Successfully Updated')
        return reverse('book-detail', kwargs={'pk':self.object.pk})

class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Book
    fields = ['booktype','bookname','location','authorname','publisher','year_publish', 'tags','bookstatus']

    def form_valid(self, form):
        # from.instance.authorname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request,f'Successfully Updated')
        return reverse('book-detail', kwargs={'pk':self.object.pk})


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book

    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True
        return False
    def get_success_url(self):
        return reverse('library-booklist')


def search(request):
    query = request.GET['q']
    print(request.GET['search_by'])
    if request.GET['search_by'] == 'title':
        found_books = Book.objects.filter(title__icontains=query)
        heading = 'Search by Title:'
        bad_result = 'No books'
    elif request.GET['search_by'] == 'author':
        found_books = Book.objects.filter(author__name__icontains=query)
        heading = 'Search by Author:'
        bad_result = 'No authors'

    context = {
        'query': query,
        'found_books': found_books,
        'heading': heading,
        'bad_result': bad_result,
    }
    return render(request, 'lib/results.html', context)
