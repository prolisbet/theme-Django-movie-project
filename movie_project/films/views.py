from django.shortcuts import render, redirect
from .models import FilmPost
from .forms import FilmPostForm


# Create your views here.
data = {
    'caption': 'Best Movies'
}


def index(request):
    return render(request, 'films/index.html', data)


def add(request):
    error = ''
    if request.method == 'POST':
        form = FilmPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films')
        else:
            error = 'Данные были заполнены некорректно'
    form = FilmPostForm()
    data['form'] = form
    data['error'] = error
    return render(request, 'films/add.html', data)


def films(request):
    film_posts = FilmPost.objects.all()
    data['film_posts'] = film_posts
    return render(request, 'films/films.html', data)
