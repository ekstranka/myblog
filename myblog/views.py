from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Service, Dotaz
from .forms import DotazForm
from . import views
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def kontakt(request):
    service = Service.objects.order_by('title')
    if request.method == "POST":
        form = DotazForm(request.POST)
        if form.is_valid():
            dotaz = form.save(commit=False)
            dotaz.created_date=timezone.now()
            dotaz.sluzba='Obecné'
            dotaz.save()
            send_mail('WEB - obecný dotaz', 'Jméno a příjmení: {0} {1}\nTelefon: {2}\nEmail: {3}\nDatum a čas: {4}\n\nDotaz:\n{5}'.format(dotaz.jmeno, dotaz.prijmeni, dotaz.mobil, dotaz.email, dotaz.created_date ,dotaz.zprava), 
                settings.EMAIL_HOST_USER, ['jaroslav.ketzer@gmail.com'], fail_silently=False)
  
            return redirect(kontakt)
    else:
        form = DotazForm()
    return render(request, 'myblog/kontakt.html', {'service': service, 'form': form})
    
def service_detail(request, title):
    sluzba = get_object_or_404(Service, title=title)
    service = Service.objects.order_by('title')
    if request.method == "POST":
        form = DotazForm(request.POST)
        if form.is_valid():
            dotaz = form.save(commit=False)
            dotaz.created_date=timezone.now()
            dotaz.sluzba=title
            dotaz.save()
            send_mail('WEB - dotaz na službu: {0}'.format(title), 'Jméno a příjmení: {0} {1}\nTelefon: {2}\nEmail: {3}\nDatum a čas: {4}\n\nDotaz:\n{5}'.format(dotaz.jmeno, dotaz.prijmeni, dotaz.mobil, dotaz.email, dotaz.created_date ,dotaz.zprava), 
                settings.EMAIL_HOST_USER, ['jaroslav.ketzer@gmail.com'], fail_silently=False)
  
            return redirect(service_detail, title=sluzba.title)
    else:
        form = DotazForm()
    return render(request, 'myblog/service_detail.html', {'service': service, 'sluzba': sluzba, 'form': form})

def services(request):
    service = Service.objects.order_by('title')
    return render(request, 'myblog/services.html', {'service': service})

def reward(request):
    service = Service.objects.order_by('title')
    return render(request, 'myblog/reward.html', {'service': service})

def profil(request):
    service = Service.objects.order_by('title')
    return render(request, 'myblog/profil.html', {'service': service})
    

