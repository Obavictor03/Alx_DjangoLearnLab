from urllib import request
from rest_framework import viewsets, permissions, filters, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from notifications.models import Notification
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardResultsSetPagination
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from notifications.utils import create_notification

# Create your views here.

# define the post behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'title']
 
 # nested comments endpoint for a post
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all().order_by('created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#  define the comment behavior.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

create_notification(
    actor=request.user,
    verb='commented on your post',
    recipient=post.author,
    target=post
)  


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=user)
    if not created:
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create a notification for the post author
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
    
    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

create_notification(
        actor=request.user,
        verb='liked your post',
        recipient=post.author,
        target=post
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=user).first()
    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    
    like.delete()
    return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)