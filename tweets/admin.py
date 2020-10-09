from django.contrib import admin

from .models import Tweet, Comment 


class CommentInline(admin.TabularInline):
    model = Comment 

class TweetAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comment)
