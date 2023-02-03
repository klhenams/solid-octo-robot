from django.contrib import admin

from .models import Dataset, Tag


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("aspect", "sentiment")
