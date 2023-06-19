from django.contrib import admin
from posts.models import UserComments , UserPost

# Register your models here. 
class AdminUserPosts(admin.ModelAdmin) : 

    list_display = ("text" , "the_user")

admin.site.register(UserPost,AdminUserPosts)

class AdminUserComments(admin.ModelAdmin) : 

    list_display = ("comment_text" , "user_comment" , "user_post")
    
admin.site.register(UserComments ,AdminUserComments)