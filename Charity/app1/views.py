import stripe
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Sum, F
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Content, Program, Contact, Donation, GuestUser


def home(request):
    registration_success = request.session.pop('registration_success', False)
    donation_success = request.session.pop('donation_success', False)
    programs = Program.objects.all()  # Retrieve the programs data from the database
    context = {
        'registration_success': registration_success,
        'donation_success': donation_success,
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
        else:
            request.session['login_failed'] = True

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
        # request.session['registration_success'] = True

        return redirect('home')  # Redirect to home page

    return render(request, 'pages/register.html')


# for donation and stripe
stripe.api_key = 'sk_test_51NFCLcL1DjYxHgevsb4mNKbO1cwy2AwPolO8DnyHgm2ZnqwFgjwHthl7mwwdafP9Oz7uqG7qKunCZp8TQkYDZCZq00Lv9TIEBt'


def stripePay(request):
    if request.method == "POST":
        amount = int(request.POST["amount"])
        program_name = request.POST.get("program")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("number")

        # Create customer
        try:
            customer = stripe.Customer.create(
                email=email,
                name=full_name,
                description="Test donation",
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            print(e)
            return HttpResponse("<h1>There was an error charging your card:</h1>" + str(e))
        except stripe.error.RateLimitError as e:
            print(e)
            return HttpResponse("<h1>Rate error!</h1>")
        except stripe.error.AuthenticationError as e:
            print(e)
            return HttpResponse("<h1>Invalid API auth!</h1>")
        except stripe.error.StripeError as e:
            print(e)
            # request.session['invalid_email'] = True
            # request.session.set_expiry(1)
            return redirect("donate")
        except stripe.error.InvalidRequestError as e:
            print(e)
            return HttpResponse("<h1>Invalid requestor!</h1>")
        except Exception as e:
            pass

        # Stripe charge
        charge = stripe.Charge.create(
            customer=customer,
            amount=int(amount) * 100,
            currency='usd',
            description="Test donation"
        )
        transRetrive = stripe.Charge.retrieve(charge["id"])
        charge.save()  # Uses the same API Key.

        # Save the form data to the Donation model
        program = Program.objects.get(program_name=program_name)
        donation = Donation.objects.create(
            user=request.user if request.user.is_authenticated else None,
            guest_user=None if request.user.is_authenticated else GuestUser.objects.create(username='guest'),
            full_name=full_name,
            email=email,
            phone=phone_number,
            amount=amount,
            program=program,
            stripeid=charge["id"]
        )
        Program.objects.filter(pk=program.pk).update(raised=F('raised') + amount)

        subject = 'Thank You for Your Donation'
        template = 'pages/email_donation'
        context = {'full_name': full_name, 'amount': amount}
        message = render_to_string(template, context)
        plain_message = strip_tags(message)
        recipient_list = [email]
        send_mail(subject, plain_message, 'handfullhandswm@gmail.com', recipient_list, html_message=message)

        # request.session['donation_success'] = True

        return redirect('home')

    # Retrieve the program names and pass them to the template context

    return render(request, "pages/donation.html", {"programs": Program.objects.all()})


def calculate_progress(raised, budget):
    if budget == 0:
        return 0
    return (raised / budget) * 100


def program_details(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    progress = calculate_progress(program.raised, program.budget)

    context = {
        'program': program,
        'progress': progress,
    }
    return render(request, 'pages/program_details.html', context)
