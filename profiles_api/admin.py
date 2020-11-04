from django.contrib import admin

from profiles_api import models
from profiles_api.models import map

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(map)
