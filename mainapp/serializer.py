from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import *

# serializer for Products


class USerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'email', 'gender', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(USerializer, self).create(validated_data)


class WTSerializer(serializers.ModelSerializer):
    workType = serializers.SerializerMethodField()

    class Meta:
        model = workTable
        fields = "__all__"

    def get_workType(self, obj):
        return obj.get_workType_display()


class ATSerializer(serializers.ModelSerializer):

    class Meta:
        model = artistTable
        fields = "__all__"
        depth = 1
