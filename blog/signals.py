import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Author


@receiver(post_save, sender=Author)
def log_user_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated user into log file"""
    logger = logging.getLogger(__name__)

    user = kwargs['instance']
    if kwargs['created']:
        logger.info("User added: %s (ID: %d)", user.user_name, user.id)
    else:
        logger.info("User updated: %s (ID: %d)", user.user_name, user.id)
