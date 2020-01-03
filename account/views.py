# users/views.py
# from rest_framework.response import Response
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.authtoken.models import Token
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate
from rest_framework import generics

from django.contrib.auth import get_user_model
from .serializers import (
    StudentCreateSerializer,
    BloodBankCreateSerializer,
    HospitalCreateSerializer,
    ParentCreateSerializer,
    SchoolCreateSerializer,
)
User = get_user_model()

# class UserListView(generics.ListAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = serializers.UserSerializer


@permission_classes((AllowAny,))
class StudentCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentCreateSerializer


@permission_classes((AllowAny,))
class BloodBankCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = BloodBankCreateSerializer


@permission_classes((AllowAny,))
class HospitalCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = HospitalCreateSerializer


@permission_classes((AllowAny,))
class ParentCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ParentCreateSerializer


@permission_classes((AllowAny,))
class SchoolCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SchoolCreateSerializer


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)
