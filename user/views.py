# user/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Profile
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


#register view and logic for user registration
class RegisterView(APIView):
    """
    API view for user registration.
    """
    permission_classes = [AllowAny] # Allow any user to register

    def post(self, request): # register a new user
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    API view for user login.
    """
    permission_classes = [AllowAny] # Allow any user to login

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                
                # Check if the profile exists, and get the profile ID if available
                try:
                    profile_id = user.profile.id
                except Profile.DoesNotExist:
                    profile_id = None  # Return None if profile doesn't exist

                return Response({
                    'message': 'Login successful!',
                    'profile_id': profile_id,  # Include the profile ID or None
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': UserSerializer(user).data,
                    'is_staff': user.is_staff,
                    'is_superuser': user.is_superuser,
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(ModelViewSet):
    """
    API viewset for user profile operations.
    """
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned profiles to the currently authenticated user.
        """
        user = self.request.user
        return Profile.objects.filter(user=user)
