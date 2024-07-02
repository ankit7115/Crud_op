from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['url', 'id', 'title', 'body', 'created', 'updated']
        extra_kwargs = {
            'url': {'view_name': 'note-detail', 'lookup_field': 'pk'}
        }
