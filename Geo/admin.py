from django.contrib import admin
from .models import Country, Region, Rivers, Mountains, Oceans

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Rivers)
admin.site.register(Mountains)
admin.site.register(Oceans)
