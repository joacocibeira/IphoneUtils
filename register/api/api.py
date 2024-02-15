from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from .serializers import RegisterSerializer, UserSerializer
from ..tasks import welcome_email
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    """
    API view for user registration.
    """
    queryset = User.objects.all()  # Queryset for the User model
    permission_classes = (AllowAny, )  # Allow any user (unauthenticated) to access this view
    serializer_class = RegisterSerializer  # Serializer for handling user registration

class LoginView(APIView):
    """
    API view for user login.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles user login and returns a token if successful.
        """
        # Retrieve user based on the provided username
        user = get_object_or_404(User, username=request.data['username'])

        # Check if the provided password is valid for the user
        if not user.check_password(request.data['password']):
            return Response({"detail": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Get or create a token for the user
        token, created = Token.objects.get_or_create(user=user)

        # Serialize the user data for the response
        serializer = UserSerializer(instance=user)

        # Return the token and user data in the response
        return Response({"token": token.key, "user": serializer.data})