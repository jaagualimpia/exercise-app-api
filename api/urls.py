from django.urls import path
from api.views import ExerciseDataEndpoint, WeightDataEndpoint

urlpatterns = [
    path("exercise", ExerciseDataEndpoint.as_view()),
    path("weight", WeightDataEndpoint.as_view())
]