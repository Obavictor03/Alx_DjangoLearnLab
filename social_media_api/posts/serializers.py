from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(author=user, **validated_data)
        return post
    
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post', write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment