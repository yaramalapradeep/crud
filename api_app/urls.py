
from django.urls import path
#from .views import movie_list,movie_details
from .views import WatchListAV, WatchListDetail,StreamPlatformAV,StreamPlatformDetail
urlpatterns = [
    path('movie-list/', WatchListAV.as_view()),
    path('movie-details/<int:id>/',WatchListDetail.as_view()),
    path('stream-list/', StreamPlatformAV.as_view()),
    path('stream-details/<int:id>/',StreamPlatformDetail.as_view())

]
