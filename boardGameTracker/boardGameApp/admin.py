from django.contrib import admin

from boardGameApp.models import BoardGame, UserProfile

# Register your models here.
admin.site.register([BoardGame, UserProfile])
