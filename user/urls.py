from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ProfileViewSet,userViewSet

# Create the router and register the ProfileViewSet
router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'users', userViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
