from django.contrib import admin
from . import models as md


@admin.register(md.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(md.Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(md.City)
class CityAdmin(admin.ModelAdmin):
    pass