from django.db import models
from django.utils.safestring import mark_safe
from common.models import CommonModel



class Banner(CommonModel):
    title = models.CharField(max_length=50,)
    context = models.TextField(blank=True, null= True,)
    image = models.ImageField(upload_to="images", blank=False, null=False,)
    on_public = models.BooleanField(default=True)
    external_link = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "배너"
        verbose_name_plural = "배너 목록"

    def __str__(self) -> str:
        return f"{self.title}({self.context})"
    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300" />')