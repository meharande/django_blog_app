from django.urls import path

from blog.api.views import (
    post_detail_view
)

app_name = 'blog'

urlpatterns =  [
    path('details/<int:pk>/', post_detail_view)
]