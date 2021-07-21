from rest_framework import serializers
from .models import Course,WishList

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','author','created_date','price','users']

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id','user','course']
