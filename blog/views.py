from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here. "my_blog" from source code.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
