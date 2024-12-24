from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import ExerciseData, WeightData
from api.serializers import ExerciseDataSerializer, WeightDataSerializer

# Create your views here.
class ExerciseDataEndpoint(APIView):
    def get(self, request):
        exercise_data = ExerciseData.objects.all()
        serialized_data = ExerciseDataSerializer(exercise_data, many=True)

        return Response(serialized_data.data)
    

class WeightDataEndpoint(APIView):
    def get(self, request):
        weight_data = WeightData.objects.all()
        serialized_data = WeightDataSerializer(weight_data, many=True)

        return Response(serialized_data.data)
