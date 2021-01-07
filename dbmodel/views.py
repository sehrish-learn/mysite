from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup(request):
    # POST method is used to send the data from client to the server
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']
        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,password=password)
        x = save()
        print("user created")
        return redirect('/')
    else:
        return render(request, 'login.html')
# Create your views here.
