from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from django.core.files.uploadedfile import UploadedFile, InMemoryUploadedFile

from .serializers import *
from .models import *

import uuid, os, io, json

### [ Modify this ] ###
class YourView(APIView):
    def get(self, request, pk, format=None):
        rv = {"data":"your data"+str(pk)} # default data
        print(rv)
        return Response(rv)
