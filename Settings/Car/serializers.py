from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from .models import Car, Comment, CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password',
            'phone_number',
            'status',
            'data_registered',
        )

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = CustomUser.objects.get(username=data['username'])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Incorrect credentials')

        if not check_password(data['password']  , user.password):
            raise serializers.ValidationError('Incorrect credentials')
        data['user'] = user
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'