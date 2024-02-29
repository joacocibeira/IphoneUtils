from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.conf import settings
from django.utils.html import strip_tags

def send_welcome_email(email, username):
    context = {
        'email': email,
        'username': username
    }

    email_subject = 'Welcome to IphoneUtils'
    
    # Render the HTML template using Django's loader
    html_email_body = loader.render_to_string('register/email_message.html', context)
    plain_email_body = strip_tags(html_email_body)
    # Create an EmailMessage instance
    email = EmailMultiAlternatives(subject=email_subject, 
                                   body=plain_email_body, 
                                   from_email=settings.DEFAULT_FROM_EMAIL, 
                                   to=[email])

    email.attach_alternative(html_email_body, 'text/html')

    # Send the email
    return email.send(fail_silently=False)