from django.apps import AppConfig


class GenresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'genres'
    verbose_name = '장르 관리'