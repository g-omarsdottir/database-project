from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
    #path("<int:pk>/like_post", views.like_detail, name="post_detail"),
    #path('posts/<int:pk>/like/', views.like_detail, name='like_post'),
    #path("<slug:slug>/like_detail/<int:pk>", views.like_detail, name="post_detail"),
     path('posts/<slug:slug>/<int:pk>/like/', views.like_detail, name='like_post'),
]
