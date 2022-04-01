from django.urls import path

from post.views import *

urlpatterns = [
    path('list/', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('delete/<int:pk>/', PostDestroyView.as_view()),
    path('update/<int:pk>/', PostUpdateView.as_view())
]