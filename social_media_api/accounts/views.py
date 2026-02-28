from urllib import request
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import permissions
from .models import CustomUser
from notifications.utils import create_notification
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()

# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    current_user = request.user
    target_user = get_object_or_404(CustomUser, id=user_id)

    if target_user == current_user:
        return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if target_user in current_user.following.all():
        return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
    
    current_user.following.add(target_user)
    return Response({'detail': f'You are now following {target_user.username}.'}, status=status.HTTP_200_OK)

create_notification(
    actor=request.user,
    verb='started following you',
    recipient=target_user,
    target=request.user
)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    current_user = request.user
    target_user = get_object_or_404(CustomUser, id=user_id)

    if target_user == current_user:
        return Response({'detail': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if target_user not in current_user.following.all():
        return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
    
    current_user.following.remove(target_user)
    return Response({'detail': f'You have unfollowed {target_user.username}.'}, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        user = CustomUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'user': response.data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key
        })
    
class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user