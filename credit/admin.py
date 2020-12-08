from django.contrib import admin

from .models import CemanetEndpoint, CallbackUrl


admin.site.register(CemanetEndpoint)
admin.site.register(CallbackUrl)
