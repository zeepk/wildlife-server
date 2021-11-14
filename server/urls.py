from django.urls import include, path

urlpatterns = [
    path('', include('wildlife.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
