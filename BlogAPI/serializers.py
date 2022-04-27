from Application.models import *
from rest_framework import serializers

'''
[
    {
       user:{

       } 
    }
]
'''

class UserSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','id'] 

    def create(self, validated_data):
        user = User(validated_data)
        user.save()
        return user



class PostSerializers(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializers()
    class Meta:
        model = Post
        fields=['title','post_image','content','category','id','soft_delete','user']
    
    def create(self, validated_data):
        new_post = Post.objects.create(**validated_data)
        new_post.user = validated_data['user']
        new_post.save()
        return new_post



class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Category
        fields = ['id','name']

    def create(self, validated_data):
        print(validated_data)
        return Category.objects.create(**validated_data)
        