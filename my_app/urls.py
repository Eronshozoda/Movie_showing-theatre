from django.urls import path
from .views import *
urlpatterns = [
    path('category_list',CategoryListView.as_view(),name="Category"),
    path('create_category',CategoryCreateView.as_view(),name="Category"),
    path('update_category/<int:pk>',CategoryUpdateView.as_view(),name="Category"),
    path('delete_category/<int:pk>',CategoryDestroyView.as_view(),name="Category"),


    path('movie_list',MovieListView.as_view(),name="Movie"),
    path('create_movie',MovieCreateView.as_view(),name="Movie"),
    path('update_movie/<int:pk>',MovieUpdateView.as_view(),name="Movie"),
    path('delete_movie/<int:pk>',MovieDestroyView.as_view(),name="Movie"),




    path('screening_list',ScreeningListView.as_view(),name="screening"),
    path('create_screening',ScreeningCreateView.as_view(),name="screening"),
    path('update_screening/<int:pk>',ScreeningUpdateView.as_view(),name="screening"),
    path('delete_screening/<int:pk>',ScreeningDestroyView.as_view(),name="screening"),


    path('review_list',ReviewListView.as_view(),name="review"),
    path('create_review',ReviewCreateView.as_view(),name="review"),
    path('update_review/<int:pk>',ReviewUpdateView.as_view(),name="review"),
    path('delete_review/<int:pk>',ReviewDestroyView.as_view(),name="review"),




    path('reservation_list',ReservationsListView.as_view(),name="reservation"),
    path('create_reservation',ReservationsCreateView.as_view(),name="reservation"),
    path('update_reservation/<int:pk>',ReservationsUpdateView.as_view(),name="reservation"),
    path('delete_reservation/<int:pk>',ReservationsDestroyView.as_view(),name="reservation"),



]
