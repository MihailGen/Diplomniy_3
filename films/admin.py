from django.contrib import admin
from .models import Film


@admin.register(Film)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director')
    search_fields = ('id', 'title', 'director')
    list_filter = ('id', 'title', 'director')

    inlines = [
       # CommentInline,
    ]

