from django.contrib import admin
from .models import Task, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'due_date')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')