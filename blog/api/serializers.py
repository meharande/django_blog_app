from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author_id', 'created_at', 'updated_at', 'deleted_at']