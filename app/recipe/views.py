"""
Views for the recipe apis
"""
# for CRUD-based models
from rest_framework import (
    viewsets,
    mixins,
)
# current auth system used
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
)
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe apis"""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    # this is needed to ensure only auth (Token) user has access to api
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # override to filter only objs linked to auth user
    def get_queryset(self):
        """Retrieve recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    # override. Most endpoints will use the detailed view
    def get_serializer_class(self):
        """Return the serializser class for request"""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    # override to map current user with created recipe
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)


# GenericVS must be defined after List<ModelMixin
# mixins.UpdateModelMixin -> updating
# mixins.DestroyModelMixin -> deleting
class TagViewSet(mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Manage tags in the database"""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # override
    def get_queryset(self):
        """Filter queryset toa authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
