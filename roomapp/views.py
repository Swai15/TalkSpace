from django.shortcuts import render

# Create your views here.
def roompage(request):
  return render (request, 'roomapp/roompage.html')

