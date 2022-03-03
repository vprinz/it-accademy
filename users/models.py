from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_email_verification(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение электронной почты для {self.user.username}'
        message = f'Для подвтерждения учетной записи для {self.user.username} перейдите по ссылке: {verification_link}'
        from_email = settings.EMAIL_HOST_USER
        emails_list = [self.user.email]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=emails_list,
        )

    def is_expired(self):
        return True if self.expiration <= now() else False
