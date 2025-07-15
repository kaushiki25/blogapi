from django.shortcuts import render

# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from rest_framework.generics import ListCreateAPIView
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import SearchFilter, OrderingFilter

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#class PostListCreateAPIView(APIView):
   # permission_classes = [IsAuthenticatedOrReadOnly]
    #def get(self, request):
       # posts = Post.objects.all()
        #serializer = PostSerializer(posts, many=True)
        #return Response(serializer.data)
    #def post(self, request):
     # serializer = PostSerializer(data=request.data)
      #if serializer.is_valid():
       # serializer.save(author=request.user)  # 👈 set author automatically
       # return Response(serializer.data, status=status.HTTP_201_CREATED)
      #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if post.author != request.user:
            return Response({"detail": "You can only delete your own posts."}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response({"detail": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if post.author != request.user:
            return Response({"detail": "You can only update your own posts."}, status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data)  # full update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if post.author != request.user:
            return Response({"detail": "You can only update your own posts."}, status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data, partial=True)  # partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MyPostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.filter(author=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)