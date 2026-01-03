from rest_framework import serializers
from .models import Folder, Note
from django.contrib.auth.models import User


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class NoteSerializer(serializers.ModelSerializer):
    folder = serializers.PrimaryKeyRelatedField(
        queryset=Folder.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Note
        fields = [
            'id',
            'folder',
            'title',
            'content',
            'color',
            'is_pinned',
            'is_archived',
            'reminder_time',
            'is_reminded',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'is_reminded',
            'created_at',
            'updated_at',
        ]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user