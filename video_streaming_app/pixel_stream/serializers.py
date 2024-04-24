from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.FileField()

    class Meta:
        model = Video
        fields = ['title', 'description', 'video_url']
