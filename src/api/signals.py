from django.db.models.signals import (
    pre_init,
    post_init,
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
    class_prepared,
    pre_migrate,
    post_migrate,
)

from django.core.signals import (
    request_started,
    request_finished,
    got_request_exception,
    setting_changed,
)

from django.dispatch import receiver

from .models import Post

# post_save.connect(Callback function, Sender)
def print_post(sender, instance, created, **kwargs):
    print("Initial Signal")
    print(instance)
    print(created)
post_save.connect(print_post, sender=Post)

# receiver(which_signal, Sender)
@receiver(post_save, sender=Post)
def print_post_alternative(sender, instance, created, **kwargs):
    print("Alternative way to send the signal")
    print(instance)
    print(created)
    