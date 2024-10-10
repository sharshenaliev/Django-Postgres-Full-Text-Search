from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.conf import settings
from products.models import Product


@receiver([post_save, post_delete], sender=Product)
def clear_cache(sender, instance, **kwargs):
    cache.delete(settings.CACHE_NAME)
