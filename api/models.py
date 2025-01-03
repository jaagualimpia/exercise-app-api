from django.db import models


class ExerciseData(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    exercise_day = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    lower_bound = models.FloatField(blank=True, null=True)
    upper_bound = models.FloatField(blank=True, null=True)
    failure = models.BooleanField(blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exercise_data'


class ExerciseDataTest(models.Model):
    exercise_day = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    unit = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    lower_bound = models.FloatField(blank=True, null=True)
    upper_bound = models.FloatField(blank=True, null=True)
    failure = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exercise_data_test'


class WeightData(models.Model):
    date = models.DateField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weight_data'