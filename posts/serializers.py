from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "title", "link", "created", "amount_of_upvotes")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "post", "author", "content", "created")
        model = Comment
