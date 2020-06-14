from django.contrib import admin
from posts.models import Post
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    list_display=['title','user','profile','created','modified']

    list_filter=['created','modified']

    class Meta:
        model = Post
    
admin.site.register(Post,ProfileAdmin)