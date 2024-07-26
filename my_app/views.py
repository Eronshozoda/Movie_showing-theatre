from django.shortcuts import render
from rest_framework import generics,filters
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



class CategoryUpdateView(generics.UpdateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class CategoryDestroyView(generics.DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer






class MovieListView(generics.ListAPIView):
    queryset=Movie.objects.all()    
    serializer_class=MovieSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=["title"]
    search_fields=['title']
    


class MovieCreateView(generics.CreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer



class MovieUpdateView(generics.UpdateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


class MovieDestroyView(generics.DestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=CategorySerializer













class ScreeningListView(generics.ListAPIView):
    queryset=Screening.objects.all()
    serializer_class=ScreeningSerializer


class ScreeningCreateView(generics.CreateAPIView):
    queryset=Screening.objects.all()
    serializer_class=ScreeningSerializer



class ScreeningUpdateView(generics.UpdateAPIView):
    queryset=Screening.objects.all()
    serializer_class=ScreeningSerializer


class ScreeningDestroyView(generics.DestroyAPIView):
    queryset=Screening.objects.all()
    serializer_class=ScreeningSerializer








class ReviewListView(generics.ListAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer



class ReviewUpdateView(generics.UpdateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer


class ReviewDestroyView(generics.DestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer






class ReservationsListView(generics.ListAPIView):
    queryset=Reservations.objects.all()
    serializer_class=ReservationsSerializer


class ReservationsCreateView(generics.CreateAPIView):
    queryset=Reservations.objects.all()
    serializer_class=ReservationsSerializer



class ReservationsUpdateView(generics.UpdateAPIView):
    queryset=Reservations.objects.all()
    serializer_class=ReservationsSerializer


class ReservationsDestroyView(generics.DestroyAPIView):
    queryset=Reservations.objects.all()
    serializer_class=ReservationsSerializer








class FeedbackListView(generics.ListAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer


class FeedbackCreateView(generics.CreateAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer



class FeedbackUpdateView(generics.UpdateAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer


class FeedbackDestroyView(generics.DestroyAPIView):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer



