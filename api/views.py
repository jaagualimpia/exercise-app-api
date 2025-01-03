from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import ExerciseData, WeightData
from api.serializers import ExerciseDataSerializer, WeightDataSerializer, ExerciseDataTestSerializer

# Create your views here.
class ExerciseDataEndpoint(APIView):
    def get(self, request):
        records = int(request.query_params.get("records"))
        print(records)

        exercise_data = ExerciseData.objects.all()[:records] if records else ExerciseData.objects.all()[:records]
        serialized_data = ExerciseDataSerializer(exercise_data, many=True)

        return Response(serialized_data.data)
    
    def post(self, request):
        print(request.data)

        return(Response(None,status=200))
    

class WeightDataEndpoint(APIView):
    def get(self, request):
        weight_data = WeightData.objects.all()
        serialized_data = WeightDataSerializer(weight_data, many=True)

        return Response(serialized_data.data)
    
class ExerciseDataTestEndpoint(APIView):
    def post(self, request):
        serializer = ExerciseDataTestSerializer(data = request.data, many = True)
        
        if serializer.is_valid():
            serializer.save()

            return Response("The records had been stored", status=201)
        
        else:
            print(serializer.errors)
            return Response(f"Se ha producido un error {serializer.error_messages}", status=400)