from celery import shared_task
from .email import send_welcome_email
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def welcome_email(email):
    logger.info("Welcome email sent")
    return send_welcome_email(email)
    
