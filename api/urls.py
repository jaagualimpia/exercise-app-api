from django.urls import path
from api.views import ExerciseDataEndpoint, WeightDataEndpoint, ExerciseDataTestEndpoint

urlpatterns = [
    path("exercise", ExerciseDataEndpoint.as_view()),
    path("weight", WeightDataEndpoint.as_view()),
    path("exercise_test", ExerciseDataTestEndpoint.as_view()),
]