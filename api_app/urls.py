
from django.urls import path
from .views import movie_list,movie_details
urlpatterns = [
    path('movie-list/', movie_list),
    path('movie-details/<int:pk>/',movie_details)

]
