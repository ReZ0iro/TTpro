from Accounts.models import UserAccounts

from posts.models import UserComments ,UserPost

from django.db.models import F, Q

from django.contrib.auth import get_user_model

#

def UserContentPostsQueries(id) : 
    """
    
    The posts and contents thath a user upload !

    """
    first_query = UserPost.objects.filter(id = id)
    
    return first_query 
