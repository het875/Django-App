from django.urls import path
from .views import UserListApiView,OTPSendView


urlpatterns = [
    # POST method for user registration
    path('users/register/', UserListApiView.submit_user_form, name='submit_user_form'),
    
    # Success page after registration
    path('registration/success/', UserListApiView.registration_success, name='registration_success'),

    # GET method for user details
    path('users/', UserListApiView.user_details_view, name='user_details'),

    # UPDATE method for updating user information
    path('users/update/<str:username>/',UserListApiView. update_user, name='update_user'),
   
    # DELETE method for deleting a user
    # path('users/delete/<str:username>/',UserListApiView.delete_user, name='delete_user'),
    path('users/delete/', UserListApiView.delete_user, name='delete_user'),


    path('api/product/add/', UserListApiView.as_view(), name='add_product'),



]
