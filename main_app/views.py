
from django.shortcuts import render, get_object_or_404
from .models import Treasure
#from django.http import HttpResponse
# Create your views here.
def index (request):
	treasures = Treasure.objects.all()
	return render(request,'index.html',{'treasures':treasures})

def gold (request):
	return render(request,'gold.html')

def detail (request, treasure_id):
	#print(treasure_id)
	treasure_detail = get_object_or_404(Treasure,pk=treasure_id)
	return render(request,'detail.html',{'treasure':treasure_detail})




