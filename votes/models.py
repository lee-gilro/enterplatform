from django.db import models
from common.models import CommonModel
# Create your models here.


class Vote(CommonModel):
    
    
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="votes",)
    question_text = models.CharField(max_length=200,)
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE, related_name="votes",)
    #choices_list = models.ManyToManyField("Choice", related_name= "votes_list", blank=True, null= True)
    class Meta:
        verbose_name = "투표 관리"
        verbose_name_plural = "투표 목록 관리"
    def __str__(self) -> str:
        return self.question_text


class Choice(CommonModel):

    question = models.ForeignKey("Vote", on_delete=models.CASCADE, related_name="choices",)
    choice_text = models.CharField(max_length=200,)
    votes = models.IntegerField(default=0)
    class Meta:
        verbose_name = "투표 답변 관리"
        verbose_name_plural = "투표 답변 목록 관리"
    def __str__(self) -> str:
        return self.choice_text