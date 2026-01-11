from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)

class Bookadmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publication_year')
    list_filter = ('title', 'publication_year')
    search_fields = ('title', 'author')
    ordering = ('title')
    list_per_page = 20