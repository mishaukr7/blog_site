from django.urls import path
from blogs.views import PostFeed, PostListView, PostDetailView, PostCreateView, ReadMarkView

app_name = 'blogs'

urlpatterns = [
    path('feed/', PostFeed.as_view(), name='feed'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/read-mark/', ReadMarkView.as_view(), name='read_mark'),
]
