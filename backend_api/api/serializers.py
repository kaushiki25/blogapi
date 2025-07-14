from rest_framework import serializers
from .models import Post

from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # now read-only

    class Meta:
        model = Post
        fields = ['id', 'title', 'author']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            password = validated_data['password']
        )
        return user