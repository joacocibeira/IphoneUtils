from rest_framework import serializers
from shortcuts.models import ClipboardQueue


class ClipboardQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipboardQueue
        fields = ['item', ]