from django.contrib import admin
from .models import films,actors,category

admin.site.register(films)
admin.site.register(actors)
admin.site.register(category)
