from django.urls import path 

from Accounts.views import *

#

urlpatterns = [

    path("AddAdmin/" , AddAdminBySuperAdmin.as_view()) , 

    path("AddUser/" , AddUserByAdmin.as_view()) ,

    path("TheUser/<int:id>/" , UserDetails.as_view()) ,

    # deActive User by admin : 
    path("DeactiveUser/<int:id>/" , DeactiveUser.as_view()) , 
    path("DeactiveUser/" , DeActiveUserByPostId.as_view() ) ,

    path("userlist/" , UsersList.as_view()) ,
]
