from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate


class UserTokenSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    password=serializers.CharField(max_length=255,style={
        'input_type':'password'
    },
    trim_whitespace=False
    )
