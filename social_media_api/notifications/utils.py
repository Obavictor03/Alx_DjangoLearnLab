from django.contrib.contenttypes.models import ContentType
from .models import Notification

def create_notification(actor, verb, recipient, target):
    if recipient == actor:
        return None 
    
    content_type = ContentType.objects.get_for_model(target)
    notification = Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        content_type=content_type,
        object_id=target.id,
        target=target
    )
    return notification