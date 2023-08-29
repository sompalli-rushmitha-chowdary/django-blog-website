from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views
urlpatterns = [
    #as class based views caannot be directly used as views .as_view is used to convert it into views
    path("", PostListView.as_view(), name='blog-home'),#looks for <app>/<model>_<viewtype>.html but that can be changed
    path("user/<str:username>/",UserPostListView.as_view(),name='user-posts'),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("post/new/", PostCreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
    path("about/", views.about, name='blog-about')
]