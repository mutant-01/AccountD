from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from accounts.models import Account, Email


class AccountSerializer(ModelSerializer):
    seen_count = serializers.IntegerField(read_only=True)
    email = serializers.PrimaryKeyRelatedField(
        queryset=Email.objects.all()
    )

    class Meta:
        model = Account
        fields = (
            'id',
            'user_field',
            'password_field',
            'address',
            'email',
            'seen_count',
        )


class EmailSerializer(ModelSerializer):

    class Meta:
        model = Email
        fields = (
            'id',
            'email_address',
            'password',
            'address',
        )
