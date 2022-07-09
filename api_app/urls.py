
from django.urls import path
#from .views import movie_list,movie_details
from .views import MovieList, MovieDetail
urlpatterns = [
    path('movie-list/', MovieList.as_view()),
    path('movie-details/<int:id>/',MovieDetail.as_view())

]
