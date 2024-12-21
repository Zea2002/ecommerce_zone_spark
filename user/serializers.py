# Description: Serializers for the user app.
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Profile,User


# Serializers for the user app.
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name') # fields to be serialized

# Serializers for the user app.register
class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True) # password confirmation

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name') # fields to be serialized

    def validate(self, attrs): # validate the password
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Passwords do not match."})
        return attrs

    def create(self, validated_data): # create a new user
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)



class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'address', 'phone', 'profile_pic', 'gender', 'date_of_birth') # fields to be serialized

    def update(self, instance, validated_data): # update the profile
        user_data = self.initial_data.get('user', None)
        if user_data:
            user_serializer = UserSerializer(instance=instance.user, data=user_data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()

        return super().update(instance, validated_data) 
