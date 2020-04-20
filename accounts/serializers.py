from rest_framework import serializers
from urllib.parse import urljoin
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import User


class MediaImageField(serializers.ImageField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        if not value:
            return None
        return urljoin(settings.MEDIA_URL, value.name)


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords must match.')
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password1']
        user = self.Meta.model.objects.create_user(**data)
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'password1', 'password2',
            'email', 'mobile', 'first_name',
            'last_name'
        )
        read_only_fields = ('id',)


class ReadOnlyAccount(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
