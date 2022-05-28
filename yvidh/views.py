from django.shortcuts import render
from . models import *
from django.views.generic.detail import DetailView
# Create your views here.
def home(request):
     gale=gal.objects.all()
     con=contact.objects.all()
     eve=event.objects.all()
     fon=font.objects.all()
     return render(request,"index.html",{"gale":gale,'con':con,'eve':eve,'fon':fon})

class eventdetails(DetailView):
     model = event
     template_name = 'eventdet.html'
     context_object_name = 'l'


