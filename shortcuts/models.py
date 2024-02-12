from django.db import models
from django.contrib.auth.models import User


class ClipboardQueue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    @classmethod
    def pop(cls, user):
        """Retrieve and delete the last added item for a given user."""
        try:
            last_item = cls.objects.filter(user=user).latest('timestamp')
            last_item.delete()
            return last_item.item
        except cls.DoesNotExist:
            return None