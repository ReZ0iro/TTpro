from rest_framework import serializers 

from posts.models import UserComments , UserPost 

#

class UserPostsSerializer(serializers.ModelSerializer) : 
    """

    For Serializing UserPosts

    """
    class Meta : 
        
        model   = UserPost

        fields  = "__all__"
class UserCommentsSerializer(serializers.ModelSerializer) : 
    """
    
    For Serializing UserComments
    
    """
    class Meta : 
        
        model   = UserComments

        fields  = "__all__"
