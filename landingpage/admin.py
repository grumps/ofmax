from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import ContactLandingPage

admin.site.register(ContactLandingPage, PageAdmin)

# Register your models here.
