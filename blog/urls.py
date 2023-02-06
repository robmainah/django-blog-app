from django.urls import path
from . import views
# from .views import (
#     PostListView,
#     PostDetailView,
# )

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<str:username>', views.UserPostListView.as_view(template_name = 'blog/user_posts.html'), name='user-posts'),
    path('new-post/', views.PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
]
