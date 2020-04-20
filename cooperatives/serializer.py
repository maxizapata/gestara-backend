from .models import Cooperative, Category
from rest_framework import serializers


class CooperativeSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Cooperative
        fields = ('name',
                  'email',
                  'short_description',
                  'description',
                  'logo',
                  'phone',
                  'web',
                  'facebook',
                  'instagram',
                  'skype',
                  'address',
                  'map_latitude',
                  'map_longitude',
                  'whatsapp',
                  'category')


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'name_pretty')
