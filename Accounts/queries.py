from django.contrib.auth import get_user_model
from django.db.models import F, Q 

# Queires : 

def UserListQueries() : 
    """
    
    It show All users that their role is USER !
    It should show for admin and SuperAdmin !

    """
    first_query     = get_user_model().objects.filter(role = 4)
    
    return first_query