from django.urls import path
from shortcuts.api.api import ClipboardQueueAPIView


urlpatterns = [
    path('clipboard/', ClipboardQueueAPIView.as_view(), name = 'clipboard-queue')
]