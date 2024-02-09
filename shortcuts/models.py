from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.id} - {self.email}"

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