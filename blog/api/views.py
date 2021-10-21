from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from blog.models import Post
from blog.api.serializers import PostSerializer

@api_view(['GET'])
def post_detail_view(request, pk):
    try:
        blog_post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if blog_post:
        serializer = PostSerializer(blog_post)
        return Response(status=status.HTTP_200_OK, data=serializer.data)