from django.contrib import admin
from .models import Post, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inline = [PostImageInline]
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
