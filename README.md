# Pixel Stream Application

## Overview
Pixel Stream Application is a Django-based video streaming application that allows users to upload, manage, and view videos.

## Installation
1. Clone the repository: https://github.com/logeshr290/video_streaming_app
2. Navigate to the project directory: cd video_streaming_app
3. Install the required dependencies: pip install -r requirements.txt

## Setup
1. Configure your database settings in `settings.py`.
2. Run migrations to create the database schema: py manage.py migrate
3. Create a superuser to access the admin interface: py manage.py createsuperuser
4. Start the development server: py manage.py runserver

## Usage
- Access the admin interface at `http://localhost:8000/admin/` to manage users, videos, and other app data.
- Visit the home page at `http://localhost:8000/` to view the video catalog and stream videos.

## API Endpoints
- `/api/videos/`: List all videos or upload a new video.
- `/api/videos/<id>/`: Retrieve, update, or delete a specific video.

## Testing
To run the tests for this application, use the following command: py manage.py test





