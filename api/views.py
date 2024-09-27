from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import ExerciseData
from api.serializers import ExerciseDataSerializer

# Create your views here.
class testEndpoint(APIView):
    def get(self, request):
        exercise_data = ExerciseData.objects.all()
        serialized_data = ExerciseDataSerializer(exercise_data, many=True)

        return Response({"data": serialized_data.data})
