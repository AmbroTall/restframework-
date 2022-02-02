from rest_framework import serializers
from register.models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id','name', 'birth_place', 'current_place')
