from django.shortcuts import render, redirect
from django.http import HttpResponse
from second_project.settings import BASE_DIR
from second_app.models import Topic, Webpage, AccessRecord, User1, UserProfileInfor, User
from .forms import FormName, UserProfileInfo_Form, UserForm


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def home(request):
    context = {
        'lines': BASE_DIR
    }
    return render(request, 'home.html', context)

@login_required
def special(request):
    return HttpResponse("You are logged in")    

@login_required   # it make sure that there is a login required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def index(request):
    context = {'text': 'Hello World', 'numbers':100}
    return render(request, 'index.html', context)
    '''
        webpage_list  = AccessRecord.objects.order_by('date')
        date_dict = {'access_records':webpage_list}
        return render(request, 'index.html', context=date_dict)
    '''


def form_name_view(request):
    users_list=User1.objects.order_by('first_name')
    name_dict= {'access_records':users_list}
    return render (request, 'form.html', context=name_dict)

def users(request):
    form_dict = FormName()
    if request.method =='POST':
        form_dict = FormName(request.POST)
        if form_dict.is_valid():
            form_dict.save(commit= True)
            print("Data has been saved")
            return redirect('/index/')
        else:
            print('Error form invalid')

    return render(request, 'users.html', {'form_dict':form_dict})

    # hidden fieldsis used to catch malicious attacks
def relative(request):
    return render (request, 'relative.html')

def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfo_Form(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user   # this sets one to one relationship
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
           
    else:
        user_form =UserForm()
        profile_form = UserProfileInfo_Form()
    return render(request, 'registration.html', 
                                        {'user_form':user_form,
                                        'profile_form':profile_form,
                                        'registered':registered})

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')

        user = authenticate(username = username, password=password)

        if user: 
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Passwrod {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'login.html', {})





















