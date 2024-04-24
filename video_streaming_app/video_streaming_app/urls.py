from django.contrib import admin
from django.urls import path, include
from pixel_stream import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('videos/upload/', views.video_upload, name='video_upload'),
    path('videos/delete/<int:pk>/', views.VideoDeleteView.as_view(), name='video_delete'),
    path('videos/list/', views.VideoListView.as_view(), name='video_list'),
    path('videos/search/', views.video_search, name='video_search'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('admin/', admin.site.urls),
    path('api/', include('pixel_stream.urls')),
]
