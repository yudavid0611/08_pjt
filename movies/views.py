from django.shortcuts import render, get_list_or_404
from django.views.decorators.http import require_safe
from django.http.response import JsonResponse
from .models import Movie

# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    pass


@require_safe
def recommended(request):
    pass