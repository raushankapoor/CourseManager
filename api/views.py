from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse,response
from django.views.decorators.csrf import csrf_exempt
from .serializers import CourseSerializer
from .models import Course,WishList
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import get_user_model

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])  
def welcome(request):
    content = {"message": "Welcome to the Couser Manager!"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return JsonResponse({'courses': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_course(request):
    User = get_user_model()
    payload = json.loads(request.body)
    user = request.user
    try:
        name = payload["name"]
        author = payload["author"]
        price = float(payload["price"])
        print("price good")
        users_ids = payload["users"]
        print("user good")
        course = Course(name=name,author=author,price=price)
        course.save()
        print(users_ids)
        for userid in users_ids:
            print(userid)
            user = User.objects.filter(id=int(userid)).first()
            print(user)
            course.users.add(user)
        course.save()
        serializer = CourseSerializer(course)
        return JsonResponse({'course': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_course(request, course_id):
    user = request.user.id
    try:
        course = Course.objects.get(id=course_id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


