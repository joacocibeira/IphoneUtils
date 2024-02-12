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

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):

        item = ClipboardQueue.pop(request.user)
        return Response({'item': item}, status=status.HTTP_200_OK)
    
    def post(self, request):
            item = request.data.get('item')

            if not item:
                return Response({"error": "Item not provided in the request data."},
                                status=status.HTTP_400_BAD_REQUEST)


            clipboard_queue_instance = ClipboardQueue.objects.create(user=request.user, item=item)

            cq_serializer = ClipboardQueueSerializer(clipboard_queue_instance)

            return Response(cq_serializer.data, status=status.HTTP_201_CREATED)