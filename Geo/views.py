from django.shortcuts import render
from django.views.generic import DetailView

from .models import Region, Country, Rivers, Oceans, Mountains


def index(request):
    return render(request, 'base.html')


class CountryDetail(DetailView):
    model = Country
    template_name = 'country_detail.html'


# Davlatlar ro'yxati
def country_list(request, region_id):
    countries = Country.objects.filter(region=region_id)
    return render(request, 'country_list.html', {'countries': countries})


# Mintaqalar ro'yxati
def region_list(request, ):
    regions = Region.objects.all()
    return render(request, 'region_list.html', {'regions': regions})


def rivers_list(request):
    rivers = Rivers.objects.all()
    return render(request, 'rivers.html', {'rivers': rivers})


def oceans_list(request):
    oceans = Oceans.objects.all()
    return render(request, 'oceans.html', {'oceans': oceans})


def mountains_list(request):
    mountains = Mountains.objects.all()
    return render(request, 'mountains.html', {'mountains': mountains})

