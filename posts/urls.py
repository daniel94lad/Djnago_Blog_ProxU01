from django.urls import path
from posts.views import (
    PostsFeedView,
    PostDetailView,
    CreatePostView,
)

app_name = 'posts'

urlpatterns =[
    path('',PostsFeedView.as_view(),name='list'),
    path('posts/new',CreatePostView.as_view(),name='create_post'),
    path('<int:pk>',PostDetailView.as_view(),name='detail'),
]