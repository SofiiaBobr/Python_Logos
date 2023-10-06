from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'published')
    list_filter = ('title', 'autor', 'create_date')
    search_fields = ('title', 'text')
    date_hierarchy = ('create_date')


# Register your models here.
admin.site.register(Post, PostAdmin)

