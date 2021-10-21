from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post

# Create your views here.

def post_detail_view(request, pk):
    try:
        blog_post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('Records not found')

    if blog_post:
        return render(request, 'blog/detail_view.html', context= {"post":blog_post})
