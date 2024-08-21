from django.contrib import admin
from . models import Tag, Comment, Blog, Categories, Newsletter


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "summary",)
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Blog, BlogAdmin)
admin.site.register(Newsletter)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Categories)
