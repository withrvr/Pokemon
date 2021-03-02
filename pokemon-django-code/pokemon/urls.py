
from pages.views import social_media_view
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('pages.urls')),

    # admin panel
    path('admin/', admin.site.urls),

    path('<str:social_media_from_url>/', social_media_view),
]
