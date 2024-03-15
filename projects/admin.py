from django.contrib import admin
from .models import Project
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'published_on')
    list_filter = ('published_on', 'category')
    prepopulated_fields = {'slug': ('title',)}