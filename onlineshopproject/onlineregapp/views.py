from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpsw = request.POST['cpsw']

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email
                                        , password=password)
        user.save();
        print('user created')
    return  render(request,'reg.html')