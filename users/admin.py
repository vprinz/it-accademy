from django.contrib import admin

from users.models import User, EmailVerification

admin.site.register(User)
admin.site.register(EmailVerification)
