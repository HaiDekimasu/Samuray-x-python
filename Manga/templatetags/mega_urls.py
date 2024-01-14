from django.conf import settings

def get_mega_url(archivo):
    """
    Obtiene la URL del archivo en Mega.

    Args:
        archivo: El nombre del archivo.

    Returns:
        La URL del archivo en Mega.
    """

    url = f"https://mega.nz/file/{settings.MEGA_KEY}/{archivo}"
    url = url.format(mode=2)
    return url.format(target='_blank')

from django import template

register = template.Library()

@register.simple_tag
def get_mega_url_download(archivo):
    """
    Obtiene la URL de descarga del archivo en Mega.

    Args:
        archivo: El nombre del archivo.

    Returns:
        La URL de descarga del archivo en Mega.
    """

    return get_mega_url(archivo)