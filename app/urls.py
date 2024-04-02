from . import views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', views.all_movies, name='all_movie'),
    path('<slug:m_link>/movie/', views.detail, name='detail'),
    path('<slug:m_link>/update/', views.update, name='update'),
    path('<slug:m_link>/delete/', views.delete, name='delete'),
    path("add_movie/", views.add_movie, name="add_movie"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("add_movie/NewCategory/", views.NewCategory, name="NewCategory"),
    path("<slug:c_link>/movie_cat/",views.all_movies,name="movie_by_category"),

]
