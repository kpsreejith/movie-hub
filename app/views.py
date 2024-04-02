from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from app.forms import MovieForm, CategoryForm
from app.models import Category, Movies
from .forms import UserProfileForm


# Create your views here.

def all_movies(request, c_link=None):
    if c_link != None:
        cat = Category.objects.get(slug=c_link)
        my_movies = Movies.objects.filter(category=cat)
    else:
        my_movies = Movies.objects.all()
    return render(request, "index.html", {"movies": my_movies})


def add_movie(request):
    if request.method == "POST":
        movie_name = request.POST.get('movie_name', )
        m_link = slugify(movie_name)
        description = request.POST.get('description', )
        release_date = request.POST.get('release_date', )
        imdb_rating = request.POST.get('imdb_rating', )
        cast = request.POST.get('cast', )
        category = request.POST.get('category', )
        categories = Category.objects.get(id=category)
        image = request.FILES['image']
        uploader = request.user
        comments_or_review = request.POST.get('comments_or_review', )
        trailer_link = request.POST.get('trailer_link', )
        movie = Movies(movie=movie_name, description=description, release_date=release_date, image=image,
                       imdb_rating=imdb_rating, cast=cast,
                       trailer_link=trailer_link, comments_or_review=comments_or_review, category=categories,
                       slug=m_link, uploader=uploader)
        movie.save()
        return redirect("app:all_movie")
    return render(request, "add.html")


def update(request, m_link):
    movie = get_object_or_404(Movies, slug=m_link)
    if request.user == movie.uploader:
        movie = Movies.objects.get(slug=m_link)
        form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, "edit.html", {'form': form, 'movie': movie})
    else:
        return render(request, "failedupdate.html")


def delete(request, m_link):
    movie = get_object_or_404(Movies, slug=m_link)
    if request.user == movie.uploader:
        if request.method == "POST":
            movie = Movies.objects.get(slug=m_link)
            movie.delete()
            return redirect('/')
        return render(request, "delete.html")
    else:
        return render(request, "failedupdate.html")


def detail(request, m_link):
    movie = Movies.objects.get(slug=m_link)
    return render(request, "detail.html", {'movie': movie})


def NewCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            slug = slugify(category)
            Category.objects.create(category=category, slug=slug)
            return redirect("app:add_movie")
    else:
        form = CategoryForm()
    return render(request, "category.html", {"form": form})


def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.user.username = username
            password = form.cleaned_data['password']
            request.user.set_password(password)
            request.user.save()

            return redirect('/')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})
