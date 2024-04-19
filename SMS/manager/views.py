from django.shortcuts import render, redirect, HttpResponse
from manager.models import user_login_info
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_page(request):
    # records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username_user = request.POST['username']
		password_user = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username_user, password=password_user)
		if user is not None:
			# login(request, user)
			messages.success(request, "You Have Been Logged In!")
			# return redirect('dashboard')
			return render(request, 'dashboard.html')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('login_pag')
	else:
		return render(request, 'login_pag.html')#, {'records':records})


# {
# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # Retrieve user from the database
#         try:
#             user = user_login_info.objects.get(Username=username)
#             if user.Password == password:
#                 # Password matched, redirect to another page
#                 return redirect('dashboard.html')
#             else:   
#                 # Password didn't match, render login page again with error message
#                 return render(request, 'login.html', {'error_message': 'Invalid username or password'})
#         except user_login_info.DoesNotExist:
#             # User not found, render login page again with error message
#             return render(request, 'login.html', {'error_message': 'Invalid username or password'})
#     else:
#         return render(request, 'login.html')
# }


# def login_page(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST) if request.POST else None  # Use form class (optional)
#         if form.is_valid():  # Validate if using form class
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(Username=username, Password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('dashboard.html')
#             else:
#                 # Handle invalid credentials (e.g., form error message)
#                 return render(request, 'login.html', {'error_message': 'Invalid username or password'})
#         else:
#             # Handle form validation errors (optional)
#             pass
#     else:
#         form = LoginForm() if request.POST else None  # Use form class (optional)
#     return render(request, 'login.html', {'form': form})

# @login_required
# def success_view(request):
#     # Display success message or redirect to another page
#     return render(request, 'dashboard.html')

