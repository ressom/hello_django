from django.contrib import admin
from .models import Shares, ShareRequest

admin.site.register([Shares, ShareRequest])
