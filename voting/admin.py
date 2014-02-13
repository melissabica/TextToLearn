# voting/admin.py
from django.contrib import admin

from .models import Choice

admin.site.register(Choice)