from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import CountryDetail

urlpatterns = [
                  path('', views.index, name='index'),
                  path('country_detail/<int:pk>', CountryDetail.as_view(), name='country_detail'),
                  path('regions/', views.region_list, name='region_list'),
                  path('oceans/', views.oceans_list, name='oceans_list'),
                  path('mountains/', views.mountains_list, name='mountains_list'),
                  path('rivers/', views.rivers_list, name='rivers_list'),
                  path('countries/<int:region_id>/', views.country_list, name='country_list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
