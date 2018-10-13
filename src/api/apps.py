from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'
    
    def ready(self):
        # Only importing this would work with decorator method
        from .signals import print_post, print_post_alternative

        # For the non-decorator method
        from django.db.models.signals import post_save
        from .models import Post
        post_save.connect(print_post, sender=Post)
