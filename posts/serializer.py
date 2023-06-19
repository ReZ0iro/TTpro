from rest_framework import serializers 

from posts.models import UserComments , UserPost 

#

class UserPostsSerializer(serializers.ModelSerializer) : 
    """

    For Serializing UserPosts

    """
    class Meta : 
        
        model = UserPost

        fields = "__all__"
    