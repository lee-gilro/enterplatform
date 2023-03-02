from django.apps import AppConfig


class TutorialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tutorial'
    verbose_name = '튜토리얼 및 큐레이션 관리'