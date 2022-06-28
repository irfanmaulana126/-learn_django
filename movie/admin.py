from django.contrib import admin
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'creator', 'created_at')
    search_fields = ('title',)
    ordering = ('title',)

admin.site.register(Movie, MovieAdmin)