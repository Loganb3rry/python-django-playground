from django.contrib import admin

from blog_app.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
