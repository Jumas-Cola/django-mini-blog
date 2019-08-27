from django.contrib import admin
from .models import Blog, Blogger, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('created',)
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(Blogger)
