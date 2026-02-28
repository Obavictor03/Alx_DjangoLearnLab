from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_repr = serializers.CharField(source='target.__str__', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target', 'target_repr', 'timestamp', 'is_read']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'timestamp']