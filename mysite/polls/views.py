from django.http import HttpResponseBadRequest,HttpResponse
from .models import User
from .serializers import PollsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status ,permissions
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import json
from .models import Product

class UserListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]
    
    #  POST Method
    def post(self, request, *args, **kwargs):
        serializer = PollsSerializer(data=request.data)
        if serializer.is_valid():
            username,mobile_number,email_id = serializer.validated_data.get('username')
            if User.objects.filter(username=username).exists():
                return Response({"error": "User with this username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(mobile_number=mobile_number).exists():
                return Response({"error": "User with this mobile_number already exists"}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email_id=email_id).exists():
                return Response({"error": "User with this email_id already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def submit_user_form(request): # -> currenty we use this function for insert user information using (POST method)
        if request.method == 'POST':
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                return render(request, 'already_registered.html')
            else:
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
                return redirect('registration_success')  # Redirect to success page
        return render(request, 'user_form.html')

    def registration_success(request):
        return render(request, 'registration_success.html')
    


    #  GET Method
    def get(self, request, *args, **kwargs): # args = what we pass as after ? for UI 
        # name = User.objects.filter(username = request.username)
        username = request.query_params.get('username')
        if username:
            # Filter users based on the provided username
            users = User.objects.filter(username=username)
            serializer = PollsSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "Please provide a username query parameter"}, status=status.HTTP_400_BAD_REQUEST)
    
    def user_details_view(request): # -> currenty we use this function for get user info using (GET method)
        username = request.GET.get('username')
        if not username:
            return render(request, 'parameter_req.html', {'error_message': 'Username parameter is required.'})
        user_profile = User.objects.filter(username=username).first()
        if not user_profile:
            return render(request, 'user_not_found.html')
        context = {'user_profile': user_profile}
        return render(request, 'user_profile.html', context)
    


    #  UPDATE Method
    def update_user(request, username):
        user = get_object_or_404(User, username=username)

        if request.method == 'POST':
            new_username = request.POST.get('username')
            new_email = request.POST.get('email')
            new_mobile_number = request.POST.get('mobile_number')

            if new_username != username and User.objects.filter(username=new_username).exists():
                error_message = f"Username '{new_username}' is already registered."
                return render(request, 'update_user.html', {'user': user, 'error_message': error_message})

            if new_email != user.email_id and User.objects.filter(email_id=new_email).exists():
                error_message = f"Email '{new_email}' is already registered."
                return render(request, 'update_user.html', {'user': user, 'error_message': error_message})

            if new_mobile_number != user.mobile_number and User.objects.filter(mobile_number=new_mobile_number).exists():
                error_message = f"Mobile number '{new_mobile_number}' is already registered."
                return render(request, 'update_user.html', {'user': user, 'error_message': error_message})

            # Update user data
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email_id = new_email
            user.mobile_number = new_mobile_number
            user.gender = request.POST.get('gender')
            user.date_of_birth = request.POST.get('date_of_birth')
            user.save()

            success_message = f"User '{username}' updated successfully."
            return render(request, 'update_user.html', {'user': user, 'success_message': success_message})

        return render(request, 'update_user.html', {'user': user})

    def delete_user(request):
        error_message = None
        success_message = None  # Initialize success_message variable

        if request.method == 'POST':
            username = request.POST.get('username')
            try:
                user = User.objects.get(username=username)
                user.delete()
                success_message = "User deleted successfully"  # Set success message
            except User.DoesNotExist:
                error_message = "User with username '{}' does not exist.".format(username)

        return render(request, 'delete_user.html', {'error_message': error_message, 'success_message': success_message})



class AddProductView(APIView):
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        shop_id = data.get('shop_id')
        is_customisable = data.get('is_customisable')
        attributes = data.get('attributes')
        category = data.get('category')
        label = data.get('label')
        images = data.get('images')
        sizes = data.get('sizes')
        colours = data.get('colours')
        fabric = data.get('fabric')
        price = data.get('price')
        description = data.get('description')
        deposit_amount = data.get('deposit_amount')
        preferred_amount = data.get('preferred_amount')
        preferred_age = data.get('preferred_age')
        preferred_season = data.get('preferred_season')

        product = Product.objects.create(
            shop_id=shop_id,
            is_customisable=is_customisable,
            attributes=attributes,
            category=category,
            label=label,
            images=images,
            sizes=sizes,
            colours=colours,
            fabric=fabric,
            price=price,
            description=description,
            deposit_amount=deposit_amount,
            preferred_amount=preferred_amount,
            preferred_age=preferred_age,
            preferred_season=preferred_season
        )

        return JsonResponse({'message': 'Product added successfully', 'product_id': product.id}, status=201)

    def get(self, request):
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)




