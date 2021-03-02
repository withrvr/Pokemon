
from pages.views import home_view, social_media_view
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # admin panel
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('home/', home_view),

    path('sm/<str:social_media_from_url>/', social_media_view),
]
