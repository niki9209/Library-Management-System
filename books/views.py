
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import BookModel


def home(request):
    return render(request, 'home.html')


def create(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        language = request.POST.get('language')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        BookModel.objects.create(
            title=title,
            author=author,
            language=language,
            price=price,
            quantity=quantity
        )

        return redirect('display')

    return render(request, 'create.html')


def display(request):

    data = BookModel.objects.all()

    return render(request, 'display.html', {'data': data})


def update(request, uid):

    book = get_object_or_404(BookModel, id=uid)

    if request.method == 'POST':

        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.language = request.POST.get('language')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')

        book.save()

        return redirect('display')

    return render(request, 'update.html', {'book': book})


def delete(request, uid):

    book = get_object_or_404(BookModel, id=uid)

    if request.method == 'POST':
        book.delete()
        return redirect('display')

    return render(request, 'delete.html', {'book': book})