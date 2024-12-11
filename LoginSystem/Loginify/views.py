from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages

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
