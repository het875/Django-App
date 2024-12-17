from django.http import HttpResponse
from .models import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import PollsSerializer
from rest_framework import permissions
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import User
from django.views import View

class UserListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    #  GET Method
    def get(self, request, *args , **kwargs): # args = what we pass as after ? for UI 
        '''
        List all the todo items for given requested user
        '''
     
        # name = User.objects.filter(username = request.username)

        username = request.query_params.get('username')  # Extract username from query parameters

        if username:
            # Filter users based on the provided username
            users = User.objects.filter(username=username)
            serializer = PollsSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a username query parameter"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    # 2. Create
    def post(self, request , *args , **kwargs):
        '''
        Create the polls with given polls data
        '''
        # data = {
        #     'first_name': request.data.get('first_name'), 
        #     'last_name': request.data.get('last_name'), 
        #     'username': request.data.get('username'),
        #     'email_id': request.data.get('email_id'),
        #     'mobile_number': request.data.get('mobile_number'),
        #     'password': request.data.get('password'),
        #     'gender': request.data.get('gender'),
        #     'date_of_birth': request.data.get('date_of_birth'),
        # }

        # serializer = PollsSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    # 2. POST method
    def submit_user_form(request):
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            mobile_number = request.POST.get('mobile_number')
            password = request.POST.get('password')
            gender = request.POST.get('gender')
            date_of_birth = request.POST.get('date_of_birth')

            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email_id=email,
                mobile_number=mobile_number,
                password=password,
                gender=gender,
                date_of_birth=date_of_birth
            )
            return redirect('registration_success')  # Redirect to a success page or home page

        return render(request, 'user_form.html')

    def registration_success(request):
        return render(request, 'registration_success.html')


# GET Method

# class ExampleView(View):
    def user_details_view(request):
        username = request.GET.get('username')
        if not username:
            # return HttpResponseBadRequest('Username parameter is required.')
            return render(request , 'parameter_req.html',{'error_message': 'Username parameter is required. het '})
        user_profile = User.objects.filter(username=username).first()
        if not user_profile:
            return render(request , 'user_not_found.html')
            # return HttpResponseBadRequest('User not found.')

        context = {
            'user_profile': user_profile,
        }
        return render(request, 'user_profile.html', context)














    # def update_user(request, username):
    #     user = get_object_or_404(User, username=username)

    #     if request.method == 'POST':
    #         # Update user fields based on form data
    #         user.first_name = request.POST.get('first_name')
    #         user.last_name = request.POST.get('last_name')
    #         user.email_id = request.POST.get('email')
    #         user.mobile_number = request.POST.get('mobile_number')
    #         user.gender = request.POST.get('gender')
    #         user.date_of_birth = request.POST.get('date_of_birth')
    #         user.save()
    #         return redirect('user_profile', username=username)  # Redirect to user profile page

    #     return render(request, 'update_user.html', {'user': user})
        

        # UPDATE method
    # path('user/<str:username>/update/', UserListApiView.update_user, name='update_user'),
    