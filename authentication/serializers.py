from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from authentication.models import User, Plan
from ttowner.models import TTowner
from rest_framework.serializers import ModelSerializer, StringRelatedField, CharField


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            "id",
            "name",
            "max_leads",
            "max_clients",
            "price"
        )


class RegisterSerializer(serializers.ModelSerializer):

    is_staff = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'photo', 'cargo', 'typeofuser', 'first_name', 'last_name',
                  'password', 'is_staff', 'parent_id', 'tabela', 'plan', 'stripe_customer_id', 'stripe_subscription_id')

    read_only_fields = ['tabela']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    plan = PlanSerializer(read_only=True)

    username_ttcompany_set = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    password = serializers.CharField(
        max_length=120, min_length=6, write_only=True)

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = User
        fields = ('id', 'email', 'username', 'password',
                  'token', 'is_staff', 'parent_id', 'typeofuser', 'username_ttcompany_set', 'plan')

        read_only_fields = ['token', 'username']


class TTownerSerializers(serializers.ModelSerializer):

    class Meta:
        model = TTowner
        fields = ('id', 'first_name',
                  'last_name', 'zipcode', 'address', 'address1', 'county', 'city',
                  'st', 'email', 'codearea', 'phone', 'username', 'tabela')

    read_only_fields = ['tabela']


class TTpaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pub_key',)

    read_only_fields = ['pub_key']
