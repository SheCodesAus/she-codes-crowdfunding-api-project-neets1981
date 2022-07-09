from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import status, permissions
from .permission import IsOwnerOrReadOnly

# Create your views here.
# users/
class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

# Post request to creat user 
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# /users/pk        
class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly
        ]
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
#  Get request    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = self.get_object(pk)
        if user.id == request.user.id:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            status=status.HTTP_401_UNAUTHORIZED)