from django.contrib import admin

from .models import Recipient, Reply, SentMessage, Organization, Group

# Register your models here.

admin.site.register(Recipient)
admin.site.register(Reply)
admin.site.register(SentMessage)
admin.site.register(Organization)
admin.site.register(Group)