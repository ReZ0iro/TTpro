from django.contrib.auth import get_user_model
from django.db.models import F, Q 

# Queires : 

def UserListQueries() : 
    """
    
    It show All users that their role is USER !
    It should show for admin and SuperAdmin !

    """
    first_query     = get_user_model().objects.filter(user_role = 4)

    return first_query
 
def TheUserDetailsQuery(id) : 
    """
    Its For Query and show the user that id is get in url or in post body to show details and 
    user data !

    """
    first_query     = get_user_model().objects.get(id = id)

    return first_query