from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Video
from .serializers import VideoSerializer
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

def landing_page(request):
    return render(request, 'video_streaming_app/landing_page.html')


@api_view(['GET','POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def video_upload(request):
    if request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Redirect to the video_list URL after successful upload
            return redirect('video_list')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        videos = Video.objects.all()  # Assuming you want to retrieve all videos
        if videos.exists():
            serializer = VideoSerializer(videos.first())  # Return the first video as a single object
            return Response(serializer.data)
        else:
            return Response({'message': 'No videos found'}, status=status.HTTP_204_NO_CONTENT)  # No Content if no videos
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class VideoListView(ListView):
    model = Video
    template_name = 'video_streaming_app/video_list.html'  # Path to your template
    context_object_name = 'videos'
    paginate_by = 10  # Number of videos per page

class VideoDetailView(DetailView):
    model = Video
    template_name = 'video_streaming_app/video_detail.html'  # Path to your template
    context_object_name = 'video'

class VideoCreateView(CreateView):
    model = Video
    template_name = 'video_streaming_app/video_form.html'  # Path to your template
    fields = ['title', 'description', 'video_url']  # Fields to include in the form
    success_url = reverse_lazy('video_list')  # URL to redirect after successful form submission

class VideoUpdateView(UpdateView):
    model = Video
    template_name = 'video_streaming_app/video_form.html'  # Path to your template
    fields = ['title', 'description', 'video_url']  # Fields to include in the form
    success_url = reverse_lazy('video_list')  # URL to redirect after successful form submission

class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'video_streaming_app/video_confirm_delete.html'  # Path to your template
    success_url = reverse_lazy('video_list')  # URL to redirect after successful deletion

def video_search(request):
    query = request.GET.get('q')
    videos = Video.objects.filter(title__icontains=query)
    return render(request, 'video_streaming_app/video_search.html', {'videos': videos, 'query': query})
