from rest_framework import serializers

from users.models import User, Location


class UserSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class LocationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

