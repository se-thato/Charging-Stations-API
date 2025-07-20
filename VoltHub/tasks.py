from celery import shared_task
from django.core.mail import send_mail

# Celery task to send an email when a charging session is complete
@shared_task
def send_session_complete_email(user_email, station_name):
    subject = 'Your Charging Session is Complete '
    message = f'Hello! Your session at {station_name} has finished. Thank you for using our service! see you soon.'
    from_email = 'thatoselepe53@gmail.com'

    send_mail(subject, message, from_email, [user_email])
    return f"Sent email to {user_email}"
