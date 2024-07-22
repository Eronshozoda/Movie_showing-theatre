from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Screening
        fields="__all__"



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"




class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations
        fields="__all__"




class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
