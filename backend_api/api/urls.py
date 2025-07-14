

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, PostListCreateAPIView, PostDetailAPIView
from .views import MyPostsAPIView  # import this

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:post_id>/', PostDetailAPIView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('my-posts/', MyPostsAPIView.as_view()),  # 👈 add this line
]
