from django.contrib import admin
from post_blog.models import Post, Comments, Categories, Feedback

# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Categories)
admin.site.register(Feedback)