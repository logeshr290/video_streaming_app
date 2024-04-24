from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Video

class VideoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.video_data = {'title': 'Sample Video', 'description': 'This is a sample video', 'video_url': 'https://www.example.com/sample-video.mp4'}
        self.response = self.client.post(reverse('video_list'), self.video_data, format='json')

    def test_create_video(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_videos(self):
        response = self.client.get(reverse('video_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.video_data['title'])
        self.assertContains(response, self.video_data['description'])
        self.assertContains(response, self.video_data['video_url'])

    def test_delete_video(self):
        video_id = self.response.data['id']
        response = self.client.delete(reverse('video_detail', kwargs={'pk': video_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Video.objects.filter(pk=video_id).exists())
