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


class MetaExpertView(generics.GenericAPIView):
    
    serializer_class = MetaExpertSerializer
    queryset = MetaExpert.objects.all()

    permission_classes = [AllowAny]

    def get(self, request,id=None, *args, **kwargs):
        if id:
            try:
                meta_obj = MetaExpert.objects.get(id=id)
            except MetaExpert.DoesNotExist:
                return Response({"message":"Meta Expert with this id not found"},status=status.HTTP_404_NOT_FOUND)
            data = self.serializer_class(meta_obj).data

            return Response(data,status=status.HTTP_200_OK)
        else:   
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        # serializer.validate_skills(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,*args,**kwargs):

        data = request.data
        
        try:
            metaexpert = MetaExpert.objects.get(id=id)
        except MetaExpert.DoesNotExist:
            return Response({"message":"MetaExpert not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(metaexpert,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpanelmentToMetaView(generics.GenericAPIView):
    serializer_class = EmpanelmentSerializer
    queryset = Empanelment.objects.all()

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        data = request.data
        empanelment_id = data.get("empanelment_id")

        try:
            empanelment = Empanelment.objects.get(id=empanelment_id)
        except Empanelment.DoesNotExist:
            return Response({"message":"Empanelment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(empanelment)
        
        empanelment = dict(serializer.data)
        del empanelment["status"]
        del empanelment["comments"]
        meta_expert_obj =  MetaExpert.objects.create(**empanelment)
        
        meta_expert_obj = MetaExpertSerializer(meta_expert_obj).data

        resp = {
            "message":"Migrated Empanelment to MetaExpert successfully",
            "data": meta_expert_obj
        }
        return Response(resp,status=status.HTTP_200_OK)