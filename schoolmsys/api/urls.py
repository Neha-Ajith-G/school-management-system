from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet, SubjectViewSet, MarkViewSet, SignUpViewSet
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views
from .serializers import UserSerializer, LoginSerializer

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'marks', MarkViewSet)
router.register(r'signup', SignUpViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', views.obtain_auth_token),
]