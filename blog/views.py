from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView
from .models import Post
from django.urls import reverse_lazy,reverse
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name= "posts_list"

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name= 'post'
