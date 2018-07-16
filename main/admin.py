from django.contrib import admin
from .models import User, Recipient, Replies, SentMessages

# Register your models here.

admin.site.register(User)
admin.site.register(Recipient)
admin.site.register(Replies)
admin.site.register(SentMessages)