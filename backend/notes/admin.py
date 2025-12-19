from django.contrib import admin
from .models import Folder, Note


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'folder',
        'is_pinned',
        'is_archived',
        'created_at',
    )
    list_filter = ('is_pinned', 'is_archived', 'created_at')
    search_fields = ('title', 'content')
