from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,  redirect


from .forms import SignUpForm, LoginForm

# Create your views here.

# @login_required(login_url='login')
def frontPage(request):
  return render (request, 'main/frontpage.html')

def signup(request):
  if request.method == "POST":
    form = SignUpForm(request.post)

    if form.is_valid():
      user = form.save()

      login(request, user)
      return redirect('frontpage')
  else:
    form = SignUpForm()
    
  return render (request, 'main/signup.html', {'form': form})


def user_login(request):
  if request.method == "POST":
    form = LoginForm(data=request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('frontpage')
  else:
      form = LoginForm()

  return render(request, 'main/login.html', {'form': form})
