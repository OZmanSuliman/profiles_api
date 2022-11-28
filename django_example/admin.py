from django.contrib import admin
from django_example import models
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)