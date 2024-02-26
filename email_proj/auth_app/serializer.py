from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class Authorise(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)