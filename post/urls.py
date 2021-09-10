
from django.urls import path
from django.urls.conf import include
from .views import PostCreateView,PostListView,PostDetailView,AddLike,PostUpdateView

app_name="post"

urlpatterns = [
    path('',PostListView.as_view(),name="index"),
    path('<int:pk>/',PostDetailView.as_view(),name="detail"),
    path('<int:pk>/edit/',PostUpdateView.as_view(),name="edit"),
    path('create/',PostCreateView.as_view(),name="create"),
    path('likes/',AddLike.as_view(),name="like")
]