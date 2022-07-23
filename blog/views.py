from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
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

class BlogCreateView(CreateView):
    model= Post
    template_name= 'blog/post_new.html'
    fields= ['title','body','author']

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'blog/post_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')