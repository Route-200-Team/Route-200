from django.contrib import admin
from .models import Trip, Destination, Note

admin.site.register(Trip)
admin.site.register(Destination)
admin.site.register(Note)