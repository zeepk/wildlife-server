from django.urls import include, path

urlpatterns = [
    path('', include('wildlife.urls')),
]
