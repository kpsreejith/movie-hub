from django.contrib import admin
from .models import Movies, Category


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category',]
    prepopulated_fields = {'slug': ('category',)}


admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie', 'slug']
    prepopulated_fields = {'slug': ('movie',)}
    list_per_page = 20


admin.site.register(Movies, MovieAdmin)
