from rest_framework import serializers
from .models import *

class YourModelSerializer(serializers.ModelSerializer):
    image1 = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = YourModel
        fields = ['id','created','integer1','text1','image1']