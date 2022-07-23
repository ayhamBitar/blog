from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView
urlpatterns = [ 
    path('<int:pk>/delte/',BlogDeleteView.as_view(),name='post_delete'),
    path('<int:pk>/edit/',BlogUpdateView.as_view(),name='post_update'),
    path('new/',BlogCreateView.as_view(), name='post_new'),
    path('<int:pk>/',BlogDetailView.as_view(), name='post_detail'),
    path('',BlogListView.as_view(),name='home'),
    
   
]