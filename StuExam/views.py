from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.views import generic
from StuExam.forms import AuthenticationForm, RegistrationForm
from StuExam.models import User


class DetailView(generic.ListView):
    template_name ='index.html'

    def get_queryset(self):
        return User.objects.all()


def login(request):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/stuexam')
    else:
        form = AuthenticationForm()
    return render_to_response('authentication_form.html', {'form': form}, context_instance=RequestContext(request))


def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/stuexam')
    else:
        form = RegistrationForm()
    return render_to_response('registration_form.html', {'form': form},context_instance=RequestContext(request) )


def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/stuexam')