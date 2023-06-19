from django.db import models

# Create your models here.
class UserPost(models.Model) : 

    text    = models.TextField(blank=False)

    the_user    = models.ForeignKey("Accounts.UserAccounts" , on_delete=models.CASCADE)

    post_upload_time    = models.DateTimeField(auto_now_add=True)

class UserComments(models.Model) : 

    comment_text    = models.TextField(blank=False) 
    
    user_comment    = models.ForeignKey("Accounts.UserAccounts", on_delete=models.CASCADE) 

    user_post       = models.ForeignKey(UserPost , on_delete=models.CASCADE, blank=False, null=False) 

    commment_upload_time     = models.DateTimeField(auto_now_add=True)


