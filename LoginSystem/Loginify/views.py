from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .serializers import UserDetailsSerializer
from rest_framework.response import Response
from rest_framework import status


def hello_world(request):
    return HttpResponse("Hello, world! Ulllalal")


# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if email already exists
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')  # Redirects back to the signup page
        
        # Save user data to the database
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')  # Redirect to login page after signup
    
    return render(request, 'signup.html')



# Login View
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if user exists
        try:
            user = UserDetails.objects.get(email=email)
            if user.password == password:
                messages.success(request, "Logged in successfully!")
                return redirect('success')  # Redirect to a success page after login
            else:
                messages.error(request, "Incorrect password.")
        except UserDetails.DoesNotExist:
            messages.error(request, "User not found.")
    
    return render(request, 'login.html')  # This ensures that the page is re-rendered with messages



# Success page view
def success(request):
    return HttpResponse("Welcome, you have logged in successfully!")


# Get all user details view
def get_all_users(request):
    if request.method == "GET":
        print("testtttt Oo00000000000")
        users = UserDetails.objects.all()
        user_list = [{"username": user.username, "email": user.email, "password": user.password} for user in users]
        return JsonResponse({"users": user_list}, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

# # Get a single user by email view
def get_user_by_email(request, email):
    if request.method == "GET":
        print("testtttt Oo00000000000")
        user = get_object_or_404(UserDetails, email=email)
        user_details = {"username": user.username, "email": user.email, "password": user.password}
        return JsonResponse({"user": user_details})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


# Update user details
@csrf_exempt
def update_user(request, email):
    if request.method == "POST":
        user = get_object_or_404(UserDetails, email=email)
        data = json.loads(request.body)
        # Remove email from the data to avoid updating it unintentionally
        if "email" in data:
            del data["email"]
        user.username = data.get("username", user.username)
        user.password = data.get("password", user.password)
        user.save()
        return JsonResponse({"message": "User details updated successfully.", "user": {"username": user.username, "email": user.email}})
    return JsonResponse({"error": "Invalid request method. Use POST."}, status=400)




@csrf_exempt
def delete_user(request, email):
    if request.method == "DELETE":
        # Check if the user with the given email exists
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({"message": f"User with email {email} deleted successfully."})
        except UserDetails.DoesNotExist:
            return JsonResponse({"error": f"User with email {email} not found."}, status=404)
    
    return JsonResponse({"error": "Invalid request method. Use DELETE."}, status=400)

