from django.contrib import admin

from vallery.core.models import Blog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description")
    search_fields = ("title", "slug", "description")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title", "slug", "description")
