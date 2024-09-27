from rest_framework import serializers

from api.models import ExerciseData

class ExerciseDataSerializer(serializers.ModelSerializer):

    class Meta:
        model  = ExerciseData
        fields = "__all__"