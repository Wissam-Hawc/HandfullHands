from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Content, Program, Contact


def home(request):
    registration_success = request.session.pop('registration_success', False)
    programs = Program.objects.all()  # Retrieve the programs data from the database
    context = {
        'registration_success': registration_success,
        'programs': programs
    }
    return render(request, 'pages/home.html', context)


def programs(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'pages/programs.html', context)


def about(request):
    content = Content.objects.get(page_name='about')  # Retrieve the content for the about page
    return render(request, 'pages/about.html', {'content': content})


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


def register(request):
    if request.method == 'POST':
        # Get the form data from the POST request
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already taken."
            return render(request, 'pages/register.html', {'error_message': error_message})

        # Perform your custom validation here
        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, 'pages/register.html', {'error_message': error_message})

        # Create a new User object and save it
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        # Set a success message
        request.session['registration_success'] = True

        return redirect('home')  # Redirect to home page

    return render(request, 'pages/register.html')
