"""
Views for the user api
"""
# rest_framework: required logic to create obs in the db
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for users"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# workflow: 
# - http req to this endpoint
# - call get_object -> (authenticated) user
# - run user through defined serializer -> result
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the auth user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # override base class to get only the user issuing the request
    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user
