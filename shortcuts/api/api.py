from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from shortcuts.api.serializers import ClipboardQueueSerializer
from shortcuts.models import ClipboardQueue, User
from django.shortcuts import get_object_or_404


class ClipboardQueueAPIView(APIView):

    def get(self, request):
        username = request.headers.get('username')

        if not username:
            return Response({"error": "Username not provided in the request header."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, email=username)


        #TODO que pasa si la cola esta vacia
        item = ClipboardQueue.pop(user)
        return Response({'item': item}, status=status.HTTP_200_OK)
    
    def post(self, request):
            username = request.headers.get('username')
            item = request.data.get('item')

            if not username or not item:
                return Response({"error": "Username or item not provided in the request data."},
                                status=status.HTTP_400_BAD_REQUEST)

            user_instance, created = User.objects.get_or_create(email=username)

            clipboard_queue_instance = ClipboardQueue.objects.create(user=user_instance, item=item)

            cq_serializer = ClipboardQueueSerializer(clipboard_queue_instance)

            return Response(cq_serializer.data, status=status.HTTP_201_CREATED)