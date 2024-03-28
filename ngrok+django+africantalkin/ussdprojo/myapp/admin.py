from django.contrib import admin
from .models import BusinessIdea,User,Account

admin.site.register(User)
admin.site.register(BusinessIdea)
admin.site.register(Account)
