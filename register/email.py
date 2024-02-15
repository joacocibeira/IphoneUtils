from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_welcome_email(email):
    context = {
        'email': email
    }

    email_subject = 'Welcome to IphoneUtils'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [email],)

    return email.send(fail_silently=False)