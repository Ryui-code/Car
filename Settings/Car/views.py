from rest_framework import viewsets, views
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .filter import CarFilter
from .models import Car, Comment, CustomUser
from .permissions import IsSellerOrReadOnly
from .serializers import CarSerializer, CommentSerializer, RegisterSerializer, LoginSerializer, CustomUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Регистрация успешна',
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Вход выполнен',
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class LoginViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.none()
    serializer_class = LoginSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.none()
    serializer_class = RegisterSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsSellerOrReadOnly]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['mark', 'region', 'year', 'paint_color', 'price']
    filterset_class = CarFilter
    permission_classes = [IsSellerOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsSellerOrReadOnly]