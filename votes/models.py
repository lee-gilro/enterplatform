from django.db import models
from common.models import CommonModel
# Create your models here.


class Vote(CommonModel):
    
    
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="votes",)
    question_text = models.CharField(max_length=200,)
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE, related_name="votes",)
    #choices_list = models.ManyToManyField("Choice", related_name= "votes_list", blank=True, null= True)
    def __str__(self) -> str:
        return self.question_text


class Choice(CommonModel):

    question = models.ForeignKey("Vote", on_delete=models.CASCADE, related_name="choices",)
    choice_text = models.CharField(max_length=200,)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text