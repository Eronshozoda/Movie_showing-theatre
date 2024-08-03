from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



# from .views import (
#     CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDestroyView,
#     MovieListView, MovieCreateView, MovieUpdateView, MovieDestroyView,
#     ScreeningListView, ScreeningCreateView, ScreeningUpdateView, ScreeningDestroyView,
#     ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDestroyView,
#     ReservationsListView, ReservationsCreateView, ReservationsUpdateView, ReservationsDestroyView,
#     FeedbackListView, FeedbackCreateView, FeedbackUpdateView, FeedbackDestroyView
# )



urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('update_category/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', CategoryDestroyView.as_view(), name='delete_category'),
    
    path('movie_list/', MovieListView.as_view(), name='movie_list'),
    path('create_movie/', MovieCreateView.as_view(), name='create_movie'),
    path('update_movie/<int:pk>/', MovieUpdateView.as_view(), name='update_movie'),
    path('delete_movie/<int:pk>/', MovieDestroyView.as_view(), name='delete_movie'),
    



    path('screening_list/', ScreeningListView.as_view(), name='screening_list'),
    path('create_screening/', ScreeningCreateView.as_view(), name='create_screening'),
    path('update_screening/<int:pk>/', ScreeningUpdateView.as_view(), name='update_screening'),
    path('delete_screening/<int:pk>/', ScreeningDestroyView.as_view(), name='delete_screening'),
    

    path('review_list/', ReviewListView.as_view(), name='review_list'),
    path('create_review/', ReviewCreateView.as_view(), name='create_review'),
    path('update_review/<int:pk>/', ReviewUpdateView.as_view(), name='update_review'),
    path('delete_review/<int:pk>/', ReviewDestroyView.as_view(), name='delete_review'),
    

    path('reservation_list/', ReservationsListView.as_view(), name='reservation_list'),
    path('create_reservation/', ReservationsCreateView.as_view(), name='create_reservation'),
    path('update_reservation/<int:pk>/', ReservationsUpdateView.as_view(), name='update_reservation'),
    path('delete_reservation/<int:pk>/', ReservationsDestroyView.as_view(), name='delete_reservation'),
    
    
    path('feedback_list/', FeedbackListView.as_view(), name='feedback_list'),
    path('create_feedback/', FeedbackCreateView.as_view(), name='create_feedback'),
    path('update_feedback/<int:pk>/', FeedbackUpdateView.as_view(), name='update_feedback'),
    path('delete_feedback/<int:pk>/', FeedbackDestroyView.as_view(), name='delete_feedback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
