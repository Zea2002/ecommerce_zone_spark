# This file is used to register the User and Profile models to the admin site.
from django.contrib import admin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active') # Display the fields in the admin site
    search_fields = ('username', 'email', 'first_name', 'last_name') # Add a search bar to the admin site
    readonly_fields = ('date_joined', 'last_login') # Make the date_joined and last_login fields read-only
    ordering = ('username',) # Order the users by their username
    filter_horizontal = () # Add a filter to the admin site
    list_filter = () # Add a list filter to the admin site

class ProfileAdmin(admin.ModelAdmin): # Create a ProfileAdmin class
    list_display = ('user', 'address', 'phone', 'profile_pic', 'gender', 'date_of_birth') # Display the fields in the admin site
    search_fields = ('user', 'address', 'phone','gender', 'date_of_birth')
    list_filter = ('user', 'address', 'phone', 'profile_pic', 'gender', 'date_of_birth')
    filter_horizontal = ()
    list_filter = ()

# Register the User and Profile models to the admin site
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

