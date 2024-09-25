from django.contrib import admin
from django.urls import path, include
from api.views import testEndpoint

urlpatterns = [
    path("base", testEndpoint.as_view())
]