from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import team

# Create your views here.
def demo(request):
    obj= Place.objects.all()
    team_obj = team.objects.all()
    return render(request,'index.html',{'result':obj,'team_res': team_obj})


