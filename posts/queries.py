from Accounts.models import UserAccounts

from posts.models import UserComments ,UserPost

from django.db.models import F, Q

from django.contrib.auth import get_user_model

#

def UserContentPostsQueries(id) : 
    """
    
    The posts and contents that a user upload !

    """
    first_query = UserPost.objects.filter(the_user = id)
    
    return first_query 
