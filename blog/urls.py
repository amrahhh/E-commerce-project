from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [    
    path('blog/', Blog_postListView.as_view(), name="blog"),
    path('single-blog/<slug:slug>/', Blog_postDetailView.as_view(), name='single_page'),
]