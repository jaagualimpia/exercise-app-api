from rest_framework import serializers

from api.models import ExerciseData, WeightData, ExerciseDataTest

class ExerciseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ExerciseData
        fields = "__all__"

class ExerciseDataTestSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ExerciseDataTest
        fields = "__all__"

class WeightDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightData
        fields = "__all__"