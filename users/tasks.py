import uuid

from django.utils.timezone import now
from datetime import timedelta

from store.celery import app
from users.models import User, EmailVerification


@app.task
def send_email_verification_task(user_id):
    try:
        print('HELLO WE ARE HERE')
        user = User.objects.get(id=user_id)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        # record.send_email_verification()
    except Exception as e:
        print(e)
