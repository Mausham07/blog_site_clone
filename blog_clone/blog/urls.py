from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/(?P<pk>\d+)/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='create_post'),
    path('post/(?P<pk>\d+)/update/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/(?P<pk>\d+)/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('post/draft/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/(?P<pk>\d+)/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/(?P<pk>\d+)/approve/', views.approve_comment, name='comment_approve'),
    path('comment/(?P<pk>\d+)/delete/', views.delete_comment, name='comment_delete'),
    path('post/(?P<pk>\d+)/publish/', views.publish_post, name='post_publish'),
]
