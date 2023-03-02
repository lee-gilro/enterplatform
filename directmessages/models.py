from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):

    users = models.ManyToManyField(
        "users.User",
        related_name= "chattingrooms",
    )
    class Meta:
        verbose_name = "채팅방 관리"
        verbose_name_plural = "채팅방 관리 목록"

    def __str__(self) -> str:
        return "Chatting Room."
    

class Message(CommonModel):

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    room = models.ForeignKey(
        "directmessages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name= "messages",
    )
    class Meta:
        verbose_name = "메시지 관리"
        verbose_name_plural = "메시지 목록 관리"
    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"