from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from shortcuts.api.serializers import ClipboardQueueSerializer
from shortcuts.models import ClipboardQueue
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ClipboardQueueAPIView(APIView):
    """
    API view for managing copy and paste functionality using a clipboard queue.
    Requires authentication with a token and permission from authenticated users.
    """

    authentication_classes = (TokenAuthentication, )  # Token-based authentication required
    permission_classes = (IsAuthenticated, )  # Permission for authenticated users only

    def get(self, request):
        """
        Handles the GET request to retrieve the next item from the clipboard queue.
        """
        item = ClipboardQueue.pop(request.user)  # Pop the next item from the clipboard queue for the user
        return Response({'item': item}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handles the POST request to add an item to the clipboard queue.
        """
        item = request.data.get('item')

        # Check if the item is provided in the request data
        if not item:
            return Response({"error": "Item not provided in the request data."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create a new instance in the ClipboardQueue model for the user and item
        clipboard_queue_instance = ClipboardQueue.objects.create(user=request.user, item=item)

        # Serialize the created instance for the response
        cq_serializer = ClipboardQueueSerializer(clipboard_queue_instance)

        return Response(cq_serializer.data, status=status.HTTP_201_CREATED)