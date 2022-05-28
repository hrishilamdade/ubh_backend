from functools import partial
from django.shortcuts import render
from .serializers import *
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class EmpanelmentView(generics.GenericAPIView):
    serializer_class = EmpanelmentSerializer
    queryset = Empanelment.objects.all()

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,*args,**kwargs):
        data = request.data
        
        try:
            empanelment = Empanelment.objects.get(id=id)
        except Empanelment.DoesNotExist:
            return Response({"message":"Empanelment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(empanelment,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)