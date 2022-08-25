from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blogs, name="list_blogs"),
    path('shutterbug', views.list_photos, name="list_photos"),
    path('exhibition/<int:id>', views.blog_details, name="blog_details"),
    path('exhibition/like/<int:id>', views.like_blog, name="like_blog")
]