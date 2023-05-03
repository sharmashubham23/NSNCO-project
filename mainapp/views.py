from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class GetProducts(APIView):

    def get(self, request):

        obj = CustomUser.objects.all()

        serializer = USerializer(obj, many=True)

        return Response(serializer.data, status=200)


class showWorks(APIView):

    def get(self, request):
        if 'artist' in request.GET:
            print("Innn")
            if request.GET['artist'] != None:
                print("Yees")

                obj = artistTable.objects.filter(
                    name__icontains=request.GET['artist'])
                serializer = ATSerializer(obj, many=True)

                return Response(serializer.data, status=200)

        if 'work_type' in request.GET:
            inp = request.GET['work_type']
            ch = ''
            if inp == 'youtube' or inp == 'Youtube':
                ch = 'Y'
            elif inp == 'Instagram' or inp == 'instagram':
                ch = 'I'
            else:
                ch = 'O'

            obj = workTable.objects.filter(workType=ch)
            serializer = WTSerializer(obj, many=True)

            return Response(serializer.data, status=200)

        obj = workTable.objects.all()

        serializer = WTSerializer(obj, many=True)

        return Response(serializer.data, status=200)


class AddUser(APIView):

    def post(self, request):
        serializer = USerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Fail to create user"})
