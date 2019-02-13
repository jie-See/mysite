from django.contrib import admin
from .models import BlogAtricles
# Register your models here.


class Blogadmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish", "body")
    list_filter = ("publish", "author")
    serch_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["publish", "author"]

admin.site.register(BlogAtricles, Blogadmin)
