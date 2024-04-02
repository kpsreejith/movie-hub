from django.shortcuts import render
from app.models import Movies
from django.db.models import Q


# Create your views here.
def SearchResult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movies.objects.all().filter(
            Q(movie__contains=query) | Q(description__contains=query) | Q(cast__contains=query) | Q(
                release_date__contains=query) )
    return render(request, 'search.html', {'query': query, 'movies': movies})
