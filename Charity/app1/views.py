from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Content, Program, Contact


def home(request):
    program = Program.objects.all()  # Call the programs function to retrieve the programs data
    context = {'programs': program}
    return render(request, 'pages/home.html', context)


def programs(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'pages/programs.html', context)


def about(request):
    # view logic goes here
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        try:
            contact = Contact(full_name=full_name, email=email, phone=phone, message=message)
            contact.save()
            print("Contact saved successfully:", contact)
            return redirect("/")  # Render a success page after saving the data
        except Exception as e:
            print("An error occurred while saving the contact:", e)
            return render(request, 'pages/contact.html')  # Render the form page with an error message
    else:
        return render(request, 'pages/contact.html')  # Render the initial form page


def details(request):
    # view logic goes here
    return render(request, 'pages/details.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect logged-in users to 'home' URL

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # if its correct it will provide a user object if no it will retrun none

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login

    return render(request, 'pages/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out!")
    return redirect("home")
