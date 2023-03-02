from django.apps import AppConfig


class BanksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'banks'
    verbose_name = '연결 은행 관리'