from django.apps import AppConfig
from django import template


class MangaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Manga'

    def ready(self):
        from .templatetags import mega_urls  # Importa la tag library
        register = template.Library()
        register.tag('get_mega_url_download', mega_urls.get_mega_url_download)  # Registra la tag
