from django.shortcuts import render
from .models import WatchList,StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView

class StreamPlatformAV(APIView):

    def get(self,request):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streams, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetail(APIView):
    def get(self, request, id):
        stream = StreamPlatform.objects.get(id=id)
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)

    def put(self, request, id):
        stream = StreamPlatform.objects.get(id=id)
        serializer = StreamPlatformSerializer(stream,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        stream = StreamPlatform.objects.get(id=id)
        stream.delete()
        return Response("stream deleted")

class WatchListAV(APIView):
    def get(self,request,*args,**kwargs):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):

        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class WatchListDetail(APIView):

    def get(self,request, id, *args,**kwargs):
        try:
            movie = WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response({'error':"Movie Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, id, *args, **kwargs):

        try:
            movie = WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response({'error': "Movie Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,*args,**kwargs):
        try:
            movie = WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response({'error': "Movie Not Found"}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         except Movie.DoesNotExist:
#             return Response(" Movie not found",status=status.HTTP_204_NO_CONTENT)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response("Movie deleted successfully",status = status.HTTP_204_NO_CONTENT)
