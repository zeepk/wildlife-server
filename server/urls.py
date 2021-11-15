from django.urls import include, path
from wildlife import views

urlpatterns = [
    path('', include('wildlife.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
    path('logout', views.logout),
]
