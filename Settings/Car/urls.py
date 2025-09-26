from django.urls import path, include
from .views import CarViewSet, CustomUserViewSet, CommentViewSet, RegisterViewSet, LoginViewSet, register_user, \
    login_user
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'users', CustomUserViewSet, basename='custom_user')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('', include(router.urls)),
]
