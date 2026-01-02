from rest_framework import viewsets, permissions
from .models import Folder, Note
from .serializers import FolderSerializer, NoteSerializer

class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Folder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(
            user=self.request.user,
            is_archived=False
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
