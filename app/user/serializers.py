"""
Serializers for the user API view
"""
# serializer: converts a given obj into a python / django model obj

from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers

# this creates & setup a django model 
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    
    # setup the model to be used, the fields to take from the request
    # the fields are first validated by the serializer 
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # overrides the behavior of the base serializer 
    # is called only after the data has been validated by the serializer
    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)

    # overrides base serializer to avoid setting password as
    # plain text. To be used by the ME api
    def update(self, instance, validated_data):
        """Update and return user"""
        # psw is an opt field in the upd request
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


# this creates & setup a basic serializer (py obj) to be used
# by the auth token api
class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for the user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and auth the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
