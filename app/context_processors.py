from app.models import Category


def MovieCategories(request):
    category_list = Category.objects.all()
    return dict(movie_cat=category_list)
