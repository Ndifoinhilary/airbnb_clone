from django.db import models
from core import models as core_model
# Create your models here.

class Conversation(core_model.TimeStampModel):
    participants = models.ManyToManyField("users.User", blank=True)
    
    
    def __str__(self):
        username = []
        for user in self.participants.all():
            username.append(user.username)
        return " , ".join(username)
    
    def count_messages(self):
        return self.messages.count()
    count_messages.short_description = "Number of messages"
    
    
    def count_participants(self):
        return self.participants.count()
    count_participants.short_description = "Number of participants"


class Message(core_model.TimeStampModel):
    message = models.TextField()
    user = models.ForeignKey('users.User', related_name='user_message', on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.user} says {self.message}'